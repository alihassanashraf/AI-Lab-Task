# AI Lab (CAI601400) — Lab 5: Adversarial Search
# Minimax & Alpha-Beta Pruning with leaf-evaluation counters
# Ali Hassan — SU92-BSAIM-F25-338

import math

# ---------------------------------------------------------
# Minimax with leaf counter (counter lines marked in PDF)
# ---------------------------------------------------------
minimax_leaves = 0                      # (1) counter declared before the function

def minimax(curDepth, nodeIndex, maxTurn, scores, targetDepth):
    global minimax_leaves
    if curDepth == targetDepth:          # leaf reached
        minimax_leaves += 1             # (2) counter incremented in the base case
        return scores[nodeIndex]
    if maxTurn:
        return max(
            minimax(curDepth + 1, nodeIndex * 2,     False, scores, targetDepth),
            minimax(curDepth + 1, nodeIndex * 2 + 1, False, scores, targetDepth),
        )
    else:
        return min(
            minimax(curDepth + 1, nodeIndex * 2,     True, scores, targetDepth),
            minimax(curDepth + 1, nodeIndex * 2 + 1, True, scores, targetDepth),
        )

# ---------------------------------------------------------
# Alpha-Beta with leaf counter — the 3 marked insertion
# points added here, same pattern as minimax:
#   (1) counter declared before the function
#   (2) counter incremented in the base case
#   (3) counter printed after the final call
# ---------------------------------------------------------
alphabeta_leaves = 0                    # (1) counter declared before the function

def alphabeta(curDepth, nodeIndex, maxTurn, scores, targetDepth, alpha, beta):
    global alphabeta_leaves
    if curDepth == targetDepth:          # leaf reached
        alphabeta_leaves += 1           # (2) counter incremented in the base case
        return scores[nodeIndex]
    if maxTurn:                          # MAX level
        best = float("-inf")
        for i in range(2):
            val = alphabeta(curDepth + 1, nodeIndex * 2 + i, False,
                            scores, targetDepth, alpha, beta)
            best = max(best, val)
            alpha = max(alpha, best)     # tighten the MAX bound
            if beta <= alpha:            # prune: MIN will never allow this
                break
        return best
    else:                                # MIN level
        best = float("inf")
        for i in range(2):
            val = alphabeta(curDepth + 1, nodeIndex * 2 + i, True,
                            scores, targetDepth, alpha, beta)
            best = min(best, val)
            beta = min(beta, best)       # tighten the MIN bound
            if beta <= alpha:            # prune: MAX will never allow this
                break
        return best

# ---------------------------------------------------------
# Task 2: run both algorithms on Tree A and Tree B
# ---------------------------------------------------------
def run_test(name, scores):
    treeDepth = math.ceil(math.log2(len(scores)))
    scores = scores + [0] * (2 ** treeDepth - len(scores))  # pad to complete tree

    global minimax_leaves, alphabeta_leaves
    minimax_leaves = 0
    mm_value = minimax(0, 0, True, scores, treeDepth)

    alphabeta_leaves = 0
    ab_value = alphabeta(0, 0, True, scores, treeDepth,
                         float("-inf"), float("inf"))

    print(f"{name} {scores}")
    print(f"  Minimax:    value = {mm_value}, leaves evaluated = {minimax_leaves}")
    print(f"  Alpha-Beta: value = {ab_value}, leaves evaluated = {alphabeta_leaves}")
    # (3) counters printed after the final calls above

treeA = [3, 5, 2, 9, 0, 7]          # Task 5.1 -> padded with zeros
treeB = [3, 5, 2, 9, 3, 5, 2, 9]    # Task 5.2

run_test("Tree A", treeA)
run_test("Tree B", treeB)

# ---------------------------------------------------------
# Task 3: branch reorder (sorted) — pruning comparison
# ---------------------------------------------------------
run_test("Tree A (sorted)", sorted(treeA + [0] * (8 - len(treeA))))
