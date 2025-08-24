def solve():
    t = int(input())
    for _ in range(t):
        a = int(input())
        arr = list(map(int, input().split()))
        
        l = sum(arr)
        arr.sort(reverse=True)
        
        r = sum(arr[i] for i in range(1, a, 2))
        
        print(l - r)

solve()