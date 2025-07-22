t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    if (n <= 2 and m <= 2) or n == 1 or m == 1:
        print("NO")
    else:
        print("YES")