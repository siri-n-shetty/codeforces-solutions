def solve():
    n = int(input())
    piles = []
    for _ in range(n):
        a, b, c, d = map(int, input().split())
        piles.append((a, b, c, d))
    
    total_moves = 0
    
    for a, b, c, d in piles:
        # Count elements that need to be moved OUT of this pile
        
        # Zeros that need to be removed from top
        zeros_to_remove = max(0, a - c)
        
        # Ones that need to be removed from bottom
        ones_to_remove = max(0, b - d)
        
        # If we need to remove ones from bottom, we must first remove ALL zeros from top
        if ones_to_remove > 0:
            # Remove all zeros from top, then remove excess ones
            total_moves += a + ones_to_remove
        else:
            # Only need to remove excess zeros from top
            total_moves += zeros_to_remove
        
        # Count elements that need to be moved INTO this pile
        zeros_to_add = max(0, c - a)
        ones_to_add = max(0, d - b)
        
        total_moves += zeros_to_add + ones_to_add
    
    # But this double counts! Each move operation moves one element from one pile to another
    # So we should only count the "move out" operations, not both "move out" and "move in"
    
    # Let's recalculate - only count moves OUT
    total_moves = 0
    
    for a, b, c, d in piles:
        # Elements that must be moved out of this pile
        zeros_to_remove = max(0, a - c)
        ones_to_remove = max(0, b - d)
        
        if ones_to_remove > 0:
            # To access ones at bottom, must remove all zeros first
            total_moves += a + ones_to_remove
        else:
            # Only remove excess zeros
            total_moves += zeros_to_remove
    
    return total_moves

def main():
    t = int(input())
    for _ in range(t):
        print(solve())

if __name__ == "__main__":
    main()