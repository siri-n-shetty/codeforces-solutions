t = int(input())
for _ in range(t):
    n = int(input())
    S = list(map(int, input().split()))

    freq = [0] * 60
    for x in S:
        freq[x] += 1

    ans = 0

    cnt2 = min(freq[0], freq[1])
    ans += cnt2 * 2
    freq[0] -= cnt2
    freq[1] -= cnt2

    cnt1 = freq[0]
    ans += cnt1
    freq[0] = 0

    for i in range(60):
        if freq[i] > 0:
            ans += i * freq[i]

    print(ans)