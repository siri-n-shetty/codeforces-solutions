t = int(input())
for _ in range(t):
    n, s = map(int, input().split())
    a = list(map(int, input().split()))
    
    sum_a = sum(a)
    cnt0 = a.count(0)
    cnt1 = a.count(1)
    cnt2 = a.count(2)
    
    T = s - sum_a
    
    if T < 0 or T == 1:
        # Rearrangement: 0s first, then 2s, then 1s
        result = [0]*cnt0 + [2]*cnt2 + [1]*cnt1
        print(" ".join(map(str, result)))
    else:
        print(-1)
