import math

def minimax(v, d, i, mx, c):
    if d == 3: c[0] += 1; return v[i]
    r = [minimax(v, d + 1, 2 * i + k, not mx, c) for k in (0, 1)]
    return max(r) if mx else min(r)

def alphabeta(v, d, i, mx, a, b, c):
    if d == 3: c[0] += 1; return v[i]
    for k in (0, 1):
        x = alphabeta(v, d + 1, 2 * i + k, not mx, a, b, c)
        if mx: a = max(a, x)
        else: b = min(b, x)
        if b <= a: break
    return a if mx else b

tests = {"Default Lab Tree": [3, 5, 2, 9, 3, 5, 2, 9],
         "Best Move Order": [5, 3, 9, 2, 2, 3, 9, 5],
         "Worst Move Order": [2, 3, 2, 3, 5, 9, 5, 9],
         "Uniform Values": [4, 4, 4, 4, 4, 4, 4, 4]}

for name, v in tests.items():
    m, p = [0], [0]
    mv = minimax(v, 0, 0, True, m)
    av = alphabeta(v, 0, 0, True, -math.inf, math.inf, p)
    print(f"Test: {name}\nArray: {v}")
    print(f"Minimax value: {mv} | Leaves Evaluated: {m[0]}")
    print(f"AlphaBeta value: {av} | Leaves Evaluated: {p[0]}")
    print("-" * 45)
