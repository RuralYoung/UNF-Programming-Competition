inputLine = 1
variables = {}

while inputLine != '0':
    inputLine = input()

    #Setting variables '='
    try:
        if inputLine.index('=') != -1:
            inputLine = inputLine.split(' ')

            variables[inputLine[0]] = inputLine[2]
        continue
    except:
        pass

    inputArray = inputLine.split(' + ')


    #Replaces the variables to numbers
    for i, x in enumerate(inputArray):
        if x in variables:
            inputArray[i] = variables[x]

    total = 0
    i = 0

    #Adds all numbers
    try:
        while i < len(inputArray):
            while inputArray[i].isdigit():
                total = total + int(inputArray.pop(i))
            i+=1
    except:
        pass

    if total != 0:
        inputArray.insert(0, total)

    if len(inputArray) == 1:
        print(inputArray[0])
    else:
        print(*inputArray, sep=" + ")