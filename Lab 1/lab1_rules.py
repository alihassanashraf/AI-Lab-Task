"""Artificial Intelligence Lab 1

Task 2: Four core tests for an extended, transparent scholarship-screening rule.

Synthetic lab assumptions:
- score must be at least 70;
- all required documents must be complete;
- identity must be verified (new named condition 1);
- the scholarship essay must be submitted (new named condition 2).

"""

from typing import Dict, List, Tuple


def evaluate_application(
    score: float,
    documents_complete: bool,
    identity_verified: bool,
    essay_submitted: bool,
) -> Tuple[str, str]:
    """Return (decision flag, reason) using four explicit conditions."""
    failed_conditions: List[str] = []

    if score < 70:
        failed_conditions.append("score is below 70")
    if not documents_complete:
        failed_conditions.append("required documents are incomplete")
    if not identity_verified:
        failed_conditions.append("identity_verified is False")
    if not essay_submitted:
        failed_conditions.append("essay_submitted is False")

    if failed_conditions:
        return "Hold", "; ".join(failed_conditions)

    return "Review", "all four conditions are satisfied"


TEST_CASES: List[Dict[str, object]] = [
    {
        "name": "pass_all_conditions",
        "score": 82,
        "documents_complete": True,
        "identity_verified": True,
        "essay_submitted": True,
        "expected": "Review",
    },
    {
        "name": "fail_identity_verification",
        "score": 82,
        "documents_complete": True,
        "identity_verified": False,
        "essay_submitted": True,
        "expected": "Hold",
    },
    {
        "name": "fail_essay_submission",
        "score": 82,
        "documents_complete": True,
        "identity_verified": True,
        "essay_submitted": False,
        "expected": "Hold",
    },
    {
        "name": "score_threshold_boundary",
        "score": 70,
        "documents_complete": True,
        "identity_verified": True,
        "essay_submitted": True,
        "expected": "Review",
    },
]


def main() -> None:
    print("CAI601400 - Lab 1: Extended Rule-Based Screening")
    print("Synthetic assumptions: score >= 70; complete documents;")
    print("identity_verified=True; essay_submitted=True.")
    print("Review = flag for a human reviewer, not an award.\n")

    all_passed = True
    for case in TEST_CASES:
        actual, reason = evaluate_application(
            score=float(case["score"]),
            documents_complete=bool(case["documents_complete"]),
            identity_verified=bool(case["identity_verified"]),
            essay_submitted=bool(case["essay_submitted"]),
        )
        passed = actual == case["expected"]
        all_passed = all_passed and passed

        print(f"Case: {case['name']}")
        print(
            "Input: "
            f"score={case['score']}, "
            f"documents_complete={case['documents_complete']}, "
            f"identity_verified={case['identity_verified']}, "
            f"essay_submitted={case['essay_submitted']}"
        )
        print(f"Expected result: {case['expected']}")
        print(f"Actual result:   {actual}")
        print(f"Reason: {reason}")
        print(f"Test status: {'PASS' if passed else 'FAIL'}")
        print("-" * 72)

    print(f"Summary: {len(TEST_CASES)} core tests; {'ALL PASSED' if all_passed else 'CHECK FAILED TESTS'}.")


if __name__ == "__main__":
    main()
