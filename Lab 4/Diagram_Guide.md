# Lab 4 - Diagram Guide

This guide explains the four diagrams included in `Lab4_Report.docx` and how to redraw them by hand in a notebook or in Microsoft Word.



## Figure 1 - Weighted directed campus graph

How to draw it:

1. Draw five circles. Put `S` on the left, `A` near the upper middle-left, `B` near the lower middle-left, `C` near the upper middle-right, and `G` on the right.
2. Draw arrows in the direction shown below. Write each edge cost next to its arrow:
   - `S -> A` has cost `1`.
   - `S -> B` has cost `4`.
   - `A -> C` has cost `2`.
   - `C -> G` has cost `3`.
   - `B -> G` has cost `5`.
3. Write the heuristic inside or below each circle: `h(S)=5`, `h(A)=4`, `h(B)=4`, `h(C)=2`, `h(G)=0`.
4. Mark `S` as START and `G` as GOAL.

Do not add extra edges. The graph is directed, so draw arrowheads.

## Figure 2 - A* search flowchart

Use these standard flowchart shapes:

- Oval: Start or End.
- Rectangle: an operation or calculation.
- Diamond: a yes/no decision.
- Arrow: direction of the process.

Draw the sequence in this order:

1. `START` (oval).
2. Initialize the OPEN/frontier list with `S`; set `g(S)=0` (rectangle).
3. Select the frontier node with the smallest `f=g+h` (rectangle).
4. Decision: `Is the selected node G?` (diamond). If **YES**, return the path and total cost (oval). If **NO**, continue.
5. Expand the selected node and calculate a tentative `g` for each neighbor (rectangle).
6. Decision: `Is tentative g lower than the known g?` (diamond). If **YES**, update the best cost and add/update that neighbor using `f=g+h` (rectangle). If **NO**, keep the existing better route (rectangle).
7. Decision: `Are frontier nodes remaining?` (diamond). If **YES**, loop back to step 3. If **NO**, end with `No path found` (oval).

The program also skips stale priority-queue entries whose `g` value is no longer the best known value. This implementation detail is explained in the report and source code.

## Figure 3 - A* frontier trace (Task 1)

Draw three boxes side by side. Each box shows the frontier after the named node is expanded. Write entries as `node(g,h,f)`.

- After expanding `S`: `A(1,4,5)`, `B(4,4,8)`. Select `A` because `5 < 8`.
- After expanding `A`: `C(3,2,5)`, `B(4,4,8)`. Select `C` because `5 < 8`.
- After expanding `C`: `G(6,0,6)`, `B(4,4,8)`. Select `G` because `6 < 8`.

The first three expanded nodes are `S`, `A`, and `C`. `G` is processed as the goal, but it is not counted as expanded because its successors are not examined.

## Figure 4 - Original vs overestimated heuristic (Task 3)

Draw two side-by-side boxes:

**Original:** `h(C)=2`; therefore `f(C)=3+2=5`. Since `B` has `f(B)=8`, A* selects `C` and returns `S -> A -> C -> G`, cost `6`.

**Modified:** `h(C)=10`; therefore `f(C)=3+10=13`. Since `B` has `f(B)=8`, A* selects `B` and returns `S -> B -> G`, cost `9`.

Write below both boxes: `Only h(C) changes from 2 to 10. The true remaining cost from C is 3.`



