t = int(input())
for _ in range(t):
    s = input()
    cnt = [0] * 26
    for c in s:
        cnt[ord(c) - ord('A')] += 1

    r = []

    r.extend(['T'] * cnt[ord('T') - ord('A')])

    r.extend(['F'] * cnt[ord('F') - ord('A')])

    for i in range(26):
        if i == ord('T') - ord('A') or i == ord('F') - ord('A'):
            continue
        r.extend([chr(ord('A') + i)] * cnt[i])

    print(''.join(r))
