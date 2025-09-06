def solve():
    t = int(input())
    for _ in range(t):
        a, b, c, d = map(int, input().split())
        

        r1, k1 = a, b

        r2, k2 = c - a, d - b

        def valid(x, y):
            return max(x, y) <= 2 * (min(x, y) + 1)

        if valid(r1, k1) and valid(r2, k2):
            print("YES")
        else:
            print("NO")

solve()