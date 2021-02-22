cases = int(input())
if cases < 1 or cases > 100:
    exit()

for x in range(cases):
    word = input()
    length = len(word)
    if length > 10:
        print(word[0] + str(length-2) + word[length-1])
    else:
        print(word)