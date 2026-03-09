def password(x):
    digit = 0
    upper = 0
    lower = 0
    valid = True
    for i in range(x):
        if i is upper:
            upper += 1
        elif i is lower:
            lower += 1
        elif i is digit:
            digit += 1
    if (upper + digit + lower) >= 8 and (upper+digit+lower) <= 12:
        valid = True
    elif upper >= 2:
        valid = True
    elif lower >= 3:
        valid = True
    elif digit >= 1:
        valid = True
    if valid == True:
        print("valid")
    else:
        print("invalid")
password("PassW0rd")