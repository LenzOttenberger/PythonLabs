text = str(input("Enter u'r text: "))
words = text.split()
wordsDict = {}
for word in words:
    word = word.lower()
    if wordsDict.get(word) == None:
        wordsDict[word] = 1
    else:
        wordsDict[word] += 1
print(wordsDict)
unic = 0
for key in wordsDict:
    if wordsDict[key] == 1:
        unic += 1
print(f'Count of unic words: {unic}')
