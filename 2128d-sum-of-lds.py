def sum_of_lds_all_subarrays(test_cases):
    results = []
    for n, p in test_cases:
        total = n * (n + 1) // 2  # Each subarray contributes at least 1
        ans = total
        for i in range(n - 1):
            if p[i] > p[i + 1]:
                ans += (i + 1) * (n - i - 1)
        results.append(ans)
    return results


# Input/Output Handling
if __name__ == "__main__":
    import sys
    input = sys.stdin.read
    data = input().split()
    
    idx = 0
    t = int(data[idx])
    idx += 1
    test_cases = []

    for _ in range(t):
        n = int(data[idx])
        idx += 1
        p = list(map(int, data[idx:idx + n]))
        idx += n
        test_cases.append((n, p))

    results = sum_of_lds_all_subarrays(test_cases)
    for res in results:
        print(res)
