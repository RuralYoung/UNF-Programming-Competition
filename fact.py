cases = int(input())
if cases < 1 or cases > 10:
    exit()

for x in range(cases):
    num = int(input())
    for y in range(1, num+1):
        num = num * y
    print(num%10)