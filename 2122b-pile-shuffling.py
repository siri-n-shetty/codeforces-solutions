def solve():
    n = int(input())
    piles = []
    for _ in range(n):
        a, b, c, d = map(int, input().split())
        piles.append((a, b, c, d))
    
    total_moves = 0
    
    for a, b, c, d in piles:
        
        zeros_to_remove = max(0, a - c)
        
        ones_to_remove = max(0, b - d)

        if ones_to_remove > 0:
            total_moves += a + ones_to_remove
        else:
            total_moves += zeros_to_remove
        
        zeros_to_add = max(0, c - a)
        ones_to_add = max(0, d - b)
        
        total_moves += zeros_to_add + ones_to_add
    

    total_moves = 0
    
    for a, b, c, d in piles:
        zeros_to_remove = max(0, a - c)
        ones_to_remove = max(0, b - d)
        
        if ones_to_remove > 0:
            total_moves += a + ones_to_remove
        else:
            total_moves += zeros_to_remove
    
    return total_moves

def main():
    t = int(input())
    for _ in range(t):
        print(solve())

if __name__ == "__main__":
    main()