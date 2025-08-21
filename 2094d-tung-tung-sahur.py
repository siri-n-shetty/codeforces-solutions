def solve(s1, s2):
    i = j = 0
    n1, n2 = len(s1), len(s2)

    while i < n1 and j < n2:
        if s1[i] != s2[j]:
            return False

        ch = s1[i]
        cnt1 = cnt2 = 0

        while i < n1 and s1[i] == ch:
            cnt1 += 1
            i += 1
        while j < n2 and s2[j] == ch:
            cnt2 += 1
            j += 1

        if 2 * cnt1 < cnt2 or cnt2 < cnt1:
            return False

    return i == n1 and j == n2

# Driver code
t = int(input())
for _ in range(t):
    s1 = input().strip()
    s2 = input().strip()
    print("YES" if solve(s1, s2) else "NO")
