"""CAI601400 - Artificial Intelligence Lab 1


"""

from typing import List, Tuple


def symbolic(score: float, documents_complete: bool) -> str:
    """Return a review flag using explicit policy conditions."""
    if documents_complete and score >= 70:
        return "Review"
    return "Hold"


def threshold(probability: float) -> str:
    """Return a review flag using a fixed demonstration threshold."""
    return "Review" if probability >= 0.70 else "Hold"


# These four examples are the manual's synthetic demonstration cases.
CASES: List[Tuple[str, int, bool, float]] = [
    ("complete_high", 82, True, 0.81),
    ("complete_low", 68, True, 0.74),
    ("incomplete_high", 91, False, 0.88),
    ("boundary", 70, True, 0.70),
]


def main() -> None:
    print("CAI601400 - Lab 1: Scholarship Screening Comparison")
    print("Review = flag for a human reviewer, not an award decision.")
    print("Probability values are synthetic inputs; no model is trained here.\n")

    print("case | symbolic | threshold | disagreement")
    for name, score, complete, probability in CASES:
        symbolic_result = symbolic(score, complete)
        threshold_result = threshold(probability)
        disagreement = symbolic_result != threshold_result
        print(name, symbolic_result, threshold_result, disagreement, sep=" | ")

    print("\nGuided example using the same input for both approaches:")
    print("symbolic(76, True):", symbolic(76, True))
    print("threshold(0.76):", threshold(0.76))

    # Sensitivity checks requested in Lab Manual Section 1.6.
    # These are separate from the four comparison cases above.
    print("\nSeparate boundary sensitivity checks:")
    print("score=69, documents_complete=True ->", symbolic(69, True))
    print("probability=0.69 ->", threshold(0.69))

    print("\nInterpretation:")
    print("The symbolic rule exposes its score and document conditions.")
    print("The threshold exposes 0.70 but not how the probability was produced.")
    print("A disagreement is a behavior difference, not evidence of model accuracy.")


if __name__ == "__main__":
    main()
