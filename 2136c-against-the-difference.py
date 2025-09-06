# from collections import Counter

# def solve():
#     t = int(input())
#     for _ in range(t):
#         n = int(input())
#         arr = list(map(int, input().split()))
        
#         freq = Counter(arr)
#         ans = 0
#         for v, cnt in freq.items():
#             ans += (cnt // v) * v
#         print(ans)

# solve()

import bisect

def solve():
    t = int(input())
    for _ in range(t):
        n = int(input())
        a = list(map(int, input().split()))
        
        pos = [[] for _ in range(n+1)]
        for i, val in enumerate(a):
            pos[val].append(i)
        
        segs = []
        for v in range(1, n+1):
            p = pos[v]
            c = len(p)

            for t in range(v, c+1):
                l = p[t-v]
                r = p[t-1]
                segs.append((r, l, v))  
        
        if not segs:
            print(0)
            continue
        
        segs.sort()
        m = len(segs)
        ends = [segs[i][0] for i in range(m)]
        starts = [segs[i][1] for i in range(m)]
        w = [segs[i][2] for i in range(m)]
        
        dp = [0] * (m+1)
        for i in range(1, m+1):
            l = starts[i-1]

            j = bisect.bisect_left(ends, l)
            dp[i] = max(dp[i-1], dp[j] + w[i-1])
        
        print(dp[m])

solve()
