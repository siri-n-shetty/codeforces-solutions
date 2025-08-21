def coins_to_destroy(test_cases):
    results = []
    for n, c, a in test_cases:
        coins = 0
        dl = []
        for x in a:
            if x > c:
                coins += 1
            else:
                v = c // x
                d = 0
                while (1 << (d + 1)) <= v:
                    d += 1
                dl.append(d)

        dl.sort()
        t = 0
        freeOK = 0
        for d in dl:
            if t <= d:
                freeOK += 1
                t += 1
        coins += len(dl) - freeOK
        results.append(coins)
    return results

# def coins_to_destroy(test_cases):
#     results = []

#     for n, c, weights in test_cases:
#         bags = weights[:]
#         coins = 0
#         while bags:
#             bags.sort()
#             w = bags.pop(0)
#             if w > c:
#                 coins += 1
#             bags = [x * 2 for x in bags]
#         results.append(coins)

#     return results

# def coins_to_destroy(test_cases):
#     results = []

#     for n, c, weights in test_cases:
#         weights.sort()
#         coins = 0
#         for i in range(n):
#             doublings = n - i - 1
#             w = weights[i]
#             final_weight = w << doublings
#             if final_weight > c:
#                 coins += 1
#         results.append(coins)

#     return results

t = int(input())
test_cases = []

for _ in range(t):
    n, c = map(int, input().split())
    weights = list(map(int, input().split()))
    test_cases.append((n, c, weights))

results = coins_to_destroy(test_cases)
for res in results:
    print(res)