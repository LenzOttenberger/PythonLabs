word = str(input('Enter word: '))
strLen = len(word)
if strLen % 2 == 0:
    if word[0:(strLen // 2)] == word[(strLen // 2):][::-1]:
        print('Poli')
    else:
        print('Not a poli')
else:
    if word[0:(strLen // 2)] == word[((strLen // 2) + 1):][::-1]:
        print('Poli')
    else:
        print('Not a poli')
