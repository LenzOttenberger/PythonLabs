def flattenList(problemList=[]):
    i = 0
    while i < len(problemList):
        if isinstance(problemList[i], list):
            sublist = problemList.pop(i)
            for item in reversed(sublist):
                problemList.insert(i, item)
        else:
            i += 1


startList = [1, 2, 3, [[4], 5, [6, 7]], 8, 9, [10]]
flattenList(startList)
print(startList)
