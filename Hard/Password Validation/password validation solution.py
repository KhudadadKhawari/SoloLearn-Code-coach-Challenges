pwd = input()

pwd_length = len(pwd)
symbols = 0
nums = 0

if pwd_length > 6:
    new_len = pwd_length
    while new_len > 0:
        new_len -= 1
        if pwd[new_len].isdigit():
            nums += 1
        elif pwd[new_len] in "!@#$%&*":
            symbols += 1

if pwd_length > 6 and nums > 1 and symbols > 1:
    print("Strong")
else:
    print("Weak")