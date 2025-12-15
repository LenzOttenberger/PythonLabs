text = str(input('Enter string of numbers: '))
listWithNumbers = text.split()
# здесь создаётся список из кучи, в которой отсеиваются повторяющиеся элементы
listWithUniqueNumbers = list(set(listWithNumbers))
firstMaxNumb = max(listWithUniqueNumbers)
# удаляем первый максимальный элемент
listWithUniqueNumbers.remove(firstMaxNumb)
secondMaxNumb = max(listWithUniqueNumbers)
print(f'Result number is {secondMaxNumb}')
