a = int(input())

while a > 0:
    basic_len = int(input())
    basic = input() 
    adding = int(input())
    adding_str = input()
    divide = input()

    for i in range(len(divide)):
        if divide[i] == "D":
            basic = basic + adding_str[i]
        else:
            basic = adding_str[i] + basic 
    
    print(basic)
    a -= 1