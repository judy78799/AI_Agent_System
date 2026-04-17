import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parent.parent.parent))

import json
from app.agent.graph import run_agent
from evaluation.metrics.scorer import keyword_match_score


def run_eval() -> dict:
    dataset_path = Path(__file__).resolve().parent.parent / "datasets" / "sample_qa.json"
    dataset = json.loads(dataset_path.read_text())

    total = len(dataset)
    success = 0
    retry = 0
    fail = 0
    empty = 0
    avg_score = 0.0

    for item in dataset:
        result = run_agent(item["question"])
        score = keyword_match_score(result.answer or "", item["expected_keywords"])
        avg_score += score

        if result.state.value == "success":
            success += 1
        elif result.state.value == "retry":
            retry += 1
        elif result.state.value == "fail":
            fail += 1
        elif result.state.value == "empty":
            empty += 1

    return {
        "total": total,
        "success_rate": success / total,
        "retry_rate": retry / total,
        "fail_rate": fail / total,
        "empty_rate": empty / total,
        "avg_score": avg_score / total,
    }

if __name__ == "__main__":
    print(run_eval())
