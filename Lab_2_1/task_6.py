listWithSomething = str(
    input('Enter elements separated by spaces (1 2 3, for example...): ')).split()
listWithDeletedDubnlicates = list(dict.fromkeys(listWithSomething))
print(listWithDeletedDubnlicates)
