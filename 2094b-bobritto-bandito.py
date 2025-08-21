t = int(input())
for _ in range(t):
    n, m, l, r = map(int, input().split())

    if m >= abs(l):
        m -= abs(l)
        ans_l = l
        ans_r = m
    else:
        ans_l = -m
        ans_r = 0

    print(ans_l, ans_r)
