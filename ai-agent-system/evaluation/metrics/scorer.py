def keyword_match_score(answer: str, expected_keywords: list[str]) -> float:
    if not answer:
        return 0.0
    matched = sum(1 for kw in expected_keywords if kw.lower() in answer.lower())
    return matched / max(len(expected_keywords), 1)
