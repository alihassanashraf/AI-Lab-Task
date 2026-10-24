# Lab 5 — Adversarial Search: Minimax & Alpha-Beta Pruning

**Course:** AI Lab (CAI601400) · Week 5
**Instructor:** Rasikh Ali
**Student:** Ali Hassan — SU92-BSAIM-F25-338

---

## What this lab is about

Two-player games can be represented as a search tree. **Minimax** explores the whole tree —
MAX picks the largest value, MIN picks the smallest — and returns the best guaranteed
outcome for MAX. **Alpha-Beta Pruning** returns the *same* answer but skips branches that
can no longer affect the result, so it evaluates fewer leaf nodes.

## Tasks

1. **Hand-trace** both trees with Minimax.
2. Add a **leaf-evaluation counter** to Minimax and Alpha-Beta and compare how many leaves each evaluates.
3. **Reorder the branches** (best-first / sorted) and compare the pruning again.

## Results (verified by running the code)

| Tree | Minimax value | Minimax leaves | Alpha-Beta value | Alpha-Beta leaves |
|---|---|---|---|---|
| Tree A `[3, 5, 2, 9, 0, 7]` (padded) | 5 | 8 | 5 | 8 — no pruning in this order |
| Tree B `[3, 5, 2, 9, 3, 5, 2, 9]` | 5 | 8 | 5 | **6** — 2 leaves pruned |
| Tree A sorted `[0, 0, 0, 2, 3, 5, 7, 9]` | 5 | 8 | 5 | **6** — ordering helps |

**Key idea:** Alpha-Beta never changes the answer — only the amount of work. Good move
ordering (best moves first) prunes the most; worst ordering prunes nothing.

Extra test cases in `task5_ai_lab.py`: Best Move Order (Alpha-Beta 5 leaves), Worst Move
Order (8 leaves — no pruning), Uniform Values (5 leaves).

## Files in this folder

| File | What it is |
|---|---|
| `manual/Lab-05-Manual.pdf` | Official lab manual for Lab 5 |
| `code/task5_ai_lab.py` | Compact Minimax + Alpha-Beta with leaf counters and 4 test cases |
| `code/Lab5_AlphaBeta_Counter_Complete.py` | Full commented implementation — Task 2 counter code + Task 3 reorder comparison |
| `code/output.txt` | Verified output of both programs |
| `report/Task-5-AI-Lab.docx` | Lab report document |
| `solution/AI_Lab5_Solution_AliHassan.pdf` | Written solution — hand traces, results table, edge case, reflection answers, viva Q&A |
| `notes/Lab5_Viva_CramSheet.md` | One-page viva cram sheet |

## How to run

```bash
cd code
python3 task5_ai_lab.py
python3 Lab5_AlphaBeta_Counter_Complete.py
```

No external libraries needed — Python 3 standard library only.
