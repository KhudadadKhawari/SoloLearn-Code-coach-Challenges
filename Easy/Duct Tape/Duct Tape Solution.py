import math
height,width = int(input()),int(input())
both_side = (height * 12)*(width * 12)*2 
print(math.ceil(both_side / 1440 ))