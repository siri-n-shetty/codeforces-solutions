def min_cost_palindrome(n, white_cost, black_cost, suits):
    total_cost = 0
    left, right = 0, n - 1

    while left < right:
        l_val = suits[left]
        r_val = suits[right]

        if l_val == 2 and r_val == 2:
            # Pick the cheaper color for both
            total_cost += 2 * min(white_cost, black_cost)
        elif l_val == 2:
            # Match to right value
            if r_val == 0:
                total_cost += white_cost
            else:
                total_cost += black_cost
        elif r_val == 2:
            # Match to left value
            if l_val == 0:
                total_cost += white_cost
            else:
                total_cost += black_cost
        else:
            # Both are fixed, they must match
            if l_val != r_val:
                return -1  # Impossible

        left += 1
        right -= 1

    # Handle middle element if n is odd
    if n % 2 == 1 and suits[n // 2] == 2:
        total_cost += min(white_cost, black_cost)

    return total_cost

# Input reading
n, a, b = map(int, input().split())
suits = list(map(int, input().split()))
print(min_cost_palindrome(n, a, b, suits))
