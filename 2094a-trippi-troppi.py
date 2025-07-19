n = int(input())
user_inputs = []
output = []

for i in range(n):
    user_inputs.append(input())

for i in range(n):
    words = user_inputs[i].split()
    initials = ''.join(word[0] for word in words)
    print(initials)
