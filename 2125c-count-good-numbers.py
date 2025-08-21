# Precomputed LCMs of {2,3,5,7} with Möbius function signs
mobius_divs = [
    (1, 1),
    (2, -1), (3, -1), (5, -1), (7, -1),
    (6, 1), (10, 1), (14, 1), (15, 1), (21, 1), (35, 1),
    (30, -1), (42, -1), (70, -1), (105, -1), (210, 1)
]

def count_good(x):
    res = 0
    for d, sign in mobius_divs:
        res += sign * (x // d)
    return res

# Read input
t = int(input())
for _ in range(t):
    l, r = map(int, input().split())
    ans = count_good(r) - count_good(l - 1)
    print(ans)
