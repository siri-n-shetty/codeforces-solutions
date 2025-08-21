import math

def solve():
    t = int(input())
    for _ in range(t):
        a, b, k = map(int, input().split())
        g = math.gcd(a, b)

        la = (a + k - 1) // k  # ceil(a / k)
        lb = (b + k - 1) // k  # ceil(b / k)

        L = max(la, lb)

        if g >= L:
            print(1)
        else:
            print(2)

solve()
