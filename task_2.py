word = input('Enter any word: ')
word = word.lower()
word = word.replace('a', '').replace('i', '').replace(
    'o', '').replace('u', '').replace('e', '')
print(word)
