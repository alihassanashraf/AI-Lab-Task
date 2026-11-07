"""AI Lab 4 - Informed Search: Heuristics and A*.

The input graph and heuristic are loaded from lab4_input.json. The script runs:
1. A* with the supplied heuristic.
2. UCS using the same priority-queue search with h(n) = 0.
3. A* after changing only h(C) from 2 to 10.

Run from this folder:
    python lab4_astar_audit.py

The program prints all results and writes the same report to lab4_output.txt.

"""

from __future__ import annotations

import heapq
import json
from math import inf
from pathlib import Path
from typing import Any, Dict, List, Tuple

Graph = Dict[str, List[Tuple[str, int]]]
Heuristic = Dict[str, int]

BASE_DIR = Path(__file__).resolve().parent
INPUT_FILE = BASE_DIR / "lab4_input.json"
OUTPUT_FILE = BASE_DIR / "lab4_output.txt"


def load_input(path: Path = INPUT_FILE) -> Tuple[Graph, Heuristic, Dict[str, int], str, str]:
    """Load and validate graph, heuristic, known true costs, start and goal."""
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except FileNotFoundError as exc:
        raise FileNotFoundError(f"Required input file not found: {path.name}") from exc
    except json.JSONDecodeError as exc:
        raise ValueError(f"Input file contains invalid JSON: {exc}") from exc

    graph: Graph = {
        str(node): [(str(nxt), int(weight)) for nxt, weight in neighbours]
        for node, neighbours in data["graph"].items()
    }
    heuristic: Heuristic = {str(node): int(value) for node, value in data["heuristic"].items()}
    true_cost: Dict[str, int] = {
        str(node): int(value) for node, value in data["true_remaining_cost"].items()
    }
    start = str(data["start"])
    goal = str(data["goal"])

    if start not in graph or goal not in graph:
        raise ValueError("Start and goal must both be keys in the graph.")
    if set(heuristic) != set(graph):
        raise ValueError("The heuristic must contain exactly one value for every graph node.")
    if set(true_cost) != set(graph):
        raise ValueError("True remaining costs must contain every graph node.")
    for node, neighbours in graph.items():
        for neighbour, weight in neighbours:
            if neighbour not in graph:
                raise ValueError(f"Neighbour {neighbour!r} from {node!r} is not a graph node.")
            if weight < 0:
                raise ValueError("This lab implementation requires non-negative edge costs.")
    return graph, heuristic, true_cost, start, goal


def path_cost(graph: Graph, path: List[str]) -> int:
    """Independently sum the edge weights along a returned path."""
    total = 0
    for current, nxt in zip(path, path[1:]):
        matching_edges = [weight for neighbour, weight in graph[current] if neighbour == nxt]
        if not matching_edges:
            raise ValueError(f"No directed edge exists from {current} to {nxt}.")
        total += matching_edges[0]
    return total


def astar(graph: Graph, heuristic: Heuristic, start: str, goal: str) -> Dict[str, Any]:
    """Run A* with a min-priority queue; all-zero h gives the UCS control.

    Queue tuples are (f, g, node, path). Python compares tuple fields in
    order: f first, then g, then node label, then path if needed. The graph's
    successor order is preserved. A node is expanded only when its
    successors are examined. The goal is processed but not expanded.
    """
    if start not in graph or goal not in graph:
        raise ValueError("Start and goal must be present in the graph.")

    priority_queue: List[Tuple[int, int, str, List[str]]] = [
        (heuristic[start], 0, start, [start])
    ]
    best_cost: Dict[str, int] = {start: 0}

    processed_nodes: List[str] = []
    expanded_nodes: List[str] = []
    expansion_details: List[Dict[str, Any]] = []
    stale_entries = 0

    while priority_queue:
        f_value, g_value, node, path = heapq.heappop(priority_queue)

        if g_value != best_cost.get(node, inf):
            stale_entries += 1
            continue

        processed_nodes.append(node)

        if node == goal:
            return {
                "found": True,
                "path": path,
                "cost": g_value,
                "processed_nodes": processed_nodes,
                "expanded_nodes": expanded_nodes,
                "expansion_details": expansion_details,
                "stale_entries": stale_entries,
            }

        expanded_nodes.append(node)

        for neighbour, edge_cost in graph.get(node, []):
            new_g = g_value + edge_cost
            if new_g < best_cost.get(neighbour, inf):
                best_cost[neighbour] = new_g
                new_f = new_g + heuristic[neighbour]
                heapq.heappush(
                    priority_queue,
                    (new_f, new_g, neighbour, path + [neighbour]),
                )

        valid_frontier = [
            (f, g, queued_node)
            for f, g, queued_node, queued_path in priority_queue
            if g == best_cost.get(queued_node, inf)
        ]
        valid_frontier.sort()
        expansion_details.append(
            {
                "node": node,
                "g": g_value,
                "h": heuristic[node],
                "f": f_value,
                "frontier": valid_frontier,
            }
        )

    return {
        "found": False,
        "path": [],
        "cost": None,
        "processed_nodes": processed_nodes,
        "expanded_nodes": expanded_nodes,
        "expansion_details": expansion_details,
        "stale_entries": stale_entries,
    }


def format_frontier(frontier: List[Tuple[int, int, str]], heuristic: Heuristic) -> str:
    if not frontier:
        return "(empty)"
    entries = []
    for f_value, g_value, node in frontier:
        h_value = heuristic[node]
        entries.append(f"{node}(g={g_value}, h={h_value}, f={f_value})")
    return ", ".join(entries)


def format_result(label: str, result: Dict[str, Any], graph: Graph) -> List[str]:
    lines = [label]
    if result["found"]:
        summed_cost = path_cost(graph, result["path"])
        lines.extend(
            [
                f"  Returned path: {' -> '.join(result['path'])}",
                f"  Cost reported by search: {result['cost']}",
                f"  Independently summed path cost: {summed_cost}",
                f"  Cost check: {'PASS' if summed_cost == result['cost'] else 'FAIL'}",
            ]
        )
    else:
        lines.extend(["  Returned path: No path found", "  Returned cost: None"])
    lines.extend(
        [
            "  Processed-node trace (goal included): "
            + (", ".join(result["processed_nodes"]) or "(none)"),
            "  Expanded nodes (goal excluded): "
            + (", ".join(result["expanded_nodes"]) or "(none)"),
            f"  Expansion count: {len(result['expanded_nodes'])}",
            f"  Stale queue entries ignored: {result['stale_entries']}",
        ]
    )
    return lines


def build_output() -> str:
    graph, supplied_h, true_cost, start, goal = load_input()
    lines: List[str] = [
        "AI LAB 4 - INFORMED SEARCH: HEURISTICS AND A*",
        "=" * 62,
        "Input file: lab4_input.json",
        "Directed graph and edge costs:",
    ]
    for node, neighbours in graph.items():
        if neighbours:
            for neighbour, weight in neighbours:
                lines.append(f"  {node} -> {neighbour}: {weight}")
        else:
            lines.append(f"  {node}: no outgoing edges")
    lines.append("Supplied heuristic: " + ", ".join(f"{n}={supplied_h[n]}" for n in graph))
    lines.append("Start: " + start + " | Goal: " + goal)
    lines.append("Queue ordering: (f, g, node, path); successor order follows the input file.")
    lines.append("")

    # Task 1: A* with the supplied heuristic and a detailed manual-style trace.
    astar_result = astar(graph, supplied_h, start, goal)
    lines.append("TASK 1 - FIRST THREE A* EXPANSIONS (SUPPLIED HEURISTIC)")
    for number, detail in enumerate(astar_result["expansion_details"][:3], start=1):
        lines.append(
            f"{number}. Selected {detail['node']}: g={detail['g']}, h={detail['h']}, "
            f"f=g+h={detail['g']}+{detail['h']}={detail['f']}"
        )
        lines.append(
            "   Frontier after expansion: "
            + format_frontier(detail["frontier"], supplied_h)
        )
    lines.append("   Selection rule: pop the valid frontier entry with the smallest f value.")
    lines.append("   Tie-breaking: lower f, then lower g, then alphabetical node label, then path.")
    lines.append("")

    # Task 2: Compare A* with UCS, using exactly the same search implementation.
    zero_h = {node: 0 for node in graph}
    ucs_result = astar(graph, zero_h, start, goal)
    lines.extend(format_result("TASK 2 - A* WITH SUPPLIED HEURISTIC", astar_result, graph))
    lines.append("")
    lines.extend(format_result("TASK 2 - UCS CONTROL (ALL HEURISTIC VALUES = 0)", ucs_result, graph))
    lines.append("")
    lines.append("TASK 2 - COMPARISON AND INTERPRETATION")
    lines.append(
        f"  A*: path cost {astar_result['cost']}; expansions {len(astar_result['expanded_nodes'])}."
    )
    lines.append(
        f"  UCS: path cost {ucs_result['cost']}; expansions {len(ucs_result['expanded_nodes'])}."
    )
    lines.append("  Both algorithms return the optimal route on this graph.")
    lines.append("  A* expands one fewer node than UCS in this particular experiment.")
    lines.append("  In UCS, B is expanded before G because g(B)=4 is less than g(G)=6.")
    lines.append("  Expanding B does not improve the best route to G, so G at cost 6 is selected next.")
    lines.append("")

    # Task 3: Change only h(C), leaving every other input unchanged.
    modified_h = dict(supplied_h)
    modified_h["C"] = 10
    modified_result = astar(graph, modified_h, start, goal)
    lines.append("TASK 3 - DELIBERATE OVERESTIMATE (ONLY h(C): 2 -> 10)")
    lines.append(f"  True remaining cost from C: {true_cost['C']}")
    lines.append(f"  Original h(C): {supplied_h['C']}")
    lines.append(f"  Modified h(C): {modified_h['C']}")
    lines.append(f"  Overestimate check: {modified_h['C']} > {true_cost['C']} = {modified_h['C'] > true_cost['C']}")
    lines.extend(format_result("  Modified A* result", modified_result, graph))
    lines.append("")

    lines.append("HEURISTIC AUDIT - SUPPLIED VALUES")
    lines.append("  Admissibility: h(n) <= true remaining cost")
    for node in graph:
        lines.append(
            f"    {node}: {supplied_h[node]} <= {true_cost[node]} "
            f"({supplied_h[node] <= true_cost[node]})"
        )
    lines.append("  Consistency: h(u) <= cost(u,v) + h(v)")
    for node, neighbours in graph.items():
        for neighbour, weight in neighbours:
            lhs = supplied_h[node]
            rhs = weight + supplied_h[neighbour]
            lines.append(f"    {node}->{neighbour}: {lhs} <= {weight}+{supplied_h[neighbour]}={rhs} ({lhs <= rhs})")
    lines.append(
        f"  Modified C->G check: 10 <= 3 + 0 = 3 ({10 <= 3}); consistency fails."
    )
    lines.append("")
    lines.append("COUNTING CONVENTION AND TRACE NOTES")
    lines.append("  A node is expanded only when its successors are examined.")
    lines.append("  The goal appears in the processed trace but is not counted as expanded.")
    lines.append("  Stale entries are ignored before processing. No stale entries occurred in these runs.")

    assert astar_result["path"] == ["S", "A", "C", "G"] and astar_result["cost"] == 6
    assert ucs_result["path"] == ["S", "A", "C", "G"] and ucs_result["cost"] == 6
    assert len(astar_result["expanded_nodes"]) == 3
    assert len(ucs_result["expanded_nodes"]) == 4
    assert modified_result["path"] == ["S", "B", "G"] and modified_result["cost"] == 9
    assert len(modified_result["expanded_nodes"]) == 3

    return "\n".join(lines) + "\n"


def main() -> None:
    output = build_output()
    print(output, end="")
    OUTPUT_FILE.write_text(output, encoding="utf-8")
    print(f"\nOutput saved to: {OUTPUT_FILE.name}")


if __name__ == "__main__":
    main()
