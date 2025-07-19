n = int(input())
a = list(map(int, input().split()))

original_one = sum(a)

if original_one == n:
    print(n-1)
    exit()

gain = [1 if x == 0 else -1 for x in a]

max_gain = current = gain[0]

for i in range(1, n):
    current = max(gain[i], current + gain[i])
    max_gain = max(max_gain, current)

print(original_one + max_gain)