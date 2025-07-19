word = input()
all_upper = True

# to check if all characters except the first one are uppercase 
for i in range(1, len(word)):
    all_upper = all_upper and word[i].isupper()

if all_upper or len(word) == 1:
    if word[0].islower():
        word = word[0].upper() + word[1:].lower()
    else:
        word = word.swapcase()

print(word)

# Input	Output
# cAPS	Caps
# Lock	Lock
# HTTP	http
# z	Z