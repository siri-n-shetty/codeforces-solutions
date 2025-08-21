def solve(n, arr, ans):
    for i in range(n):
        for j in range(n):
            ans[i + j + 1] = arr[i][j]

    num_rem = 0
    for i in range(2 * n):
        num_rem ^= ans[i]
    for i in range(1, 2 * n + 1):
        num_rem ^= i

    for i in range(2 * n):
        if ans[i] == 0:
            ans[i] = num_rem
            break

t = int(input())
for _ in range(t):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    ans = [0] * (2 * n)

    solve(n, arr, ans)

    print(*ans)
