firstWord = str(input('Enter first word: ')).lower()
secondWord = str(input('Enter second word: ')).lower()
print(sorted(list(firstWord)) == sorted(list(secondWord)))
