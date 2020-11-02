sentences = input().split()
pigLatin = ""

for sentence  in sentences:
    pigLatin += sentence[1:] + sentence[0]+"ay "

print(pigLatin)