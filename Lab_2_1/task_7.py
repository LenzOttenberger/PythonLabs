textString = str(input('Enter your string: '))
listForNewString = []
currentCountOfSymbol = 0
for i in range(len(textString)):
    if i == 0:
        listForNewString.append(textString[i])
        currentCountOfSymbol += 1
    elif textString[i] == listForNewString[-1]:
        currentCountOfSymbol += 1
    else:
        listForNewString.append(currentCountOfSymbol)
        currentCountOfSymbol = 1
        listForNewString.append(textString[i])
listForNewString.append(currentCountOfSymbol)
cuttedFinalString = ''.join(map(str, listForNewString))
print(cuttedFinalString)
