## Problem

LLM applications are inherently non-deterministic, which makes reliability,
failure handling, and debugging difficult in production settings.

## Approach

This project implements a state-aware RAG agent system where execution flow is
controlled by explicit states rather than implicit LLM behavior.

## Key Design Principles

- State-driven execution flow
- Separate validation layer for response quality control
- Retry and fallback policies for failure handling
- Evaluation harness for measurable system reliability
- Observability for tracing latency and failure patterns

## Why It Matters

The goal of this project is not to build a generic chatbot, but to demonstrate
how reliable LLM systems can be designed, validated, and operated.
