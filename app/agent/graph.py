from typing import Literal

from langgraph.graph import END, START, StateGraph

from app.agent.nodes.executor import executor_node
from app.agent.nodes.fallback import fallback_node
from app.agent.nodes.planner import planner_node
from app.agent.nodes.validator import validator_node
from app.agent.state import AgentContext, RunState


def route_after_validator(
    ctx: AgentContext,
) -> Literal["executor", "fallback", "__end__"]:
    if ctx.state == RunState.RETRY:
        return "executor"

    if ctx.state == RunState.EMPTY:
        return "fallback"

    return "__end__"


def build_graph():
    graph = StateGraph(AgentContext)

    graph.add_node("planner", planner_node)
    graph.add_node("executor", executor_node)
    graph.add_node("validator", validator_node)
    graph.add_node("fallback", fallback_node)

    graph.add_edge(START, "planner")
    graph.add_edge("planner", "executor")
    graph.add_edge("executor", "validator")

    graph.add_conditional_edges(
        "validator",
        route_after_validator,
        {
            "executor": "executor",
            "fallback": "fallback",
            "__end__": END,
        },
    )

    graph.add_edge("fallback", END)

    return graph.compile()


agent_graph = build_graph()


def run_agent(query: str) -> AgentContext:
    initial_state = AgentContext(query=query)
    return agent_graph.invoke(initial_state)
