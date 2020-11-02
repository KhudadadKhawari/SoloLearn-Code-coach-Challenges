txt = input()

for a in txt[::-1]:
    if a.isalpha() or a.isspace():
        print(a, end = '')