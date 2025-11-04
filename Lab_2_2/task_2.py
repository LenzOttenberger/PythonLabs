def dictionariesMerging(dict1={}, dict2={}):
    mergedDict = {}
    for key, value in dict1.items():
        mergedDict[key] = value
    for key, value in dict2.items():
        if key in mergedDict and isinstance(mergedDict[key], dict):
            mergedDict[key] = dictionariesMerging(mergedDict[key], dict2[key])
        else:
            mergedDict[key] = value
    return mergedDict


dict1 = {'a': 1, 'b': {'c': 1, 'f': 4}}
dict2 = {'d': 1, 'b': {'c': 2, 'e': 3}, 'n': {'y': 5}}
mergedDict = dictionariesMerging(dict1, dict2)
print(mergedDict)
