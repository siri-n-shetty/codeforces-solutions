def solve():
    t = int(input())
    for _ in range(t):
        n = int(input())
        gears = list(map(int, input().split()))
        
        # If there's any duplicate gear size → YES
        if len(gears) != len(set(gears)):
            print("YES")
        else:
            print("NO")

solve()