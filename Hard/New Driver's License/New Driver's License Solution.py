name = input()
agent = int(input())
people = input().split()

position = 0

for person in people:
    if person < name:
        position += 1

time = 20*(1+position // agent )

print(time)