def count_words(text: str) -> int:
    if not isinstance(text, str):
        raise TypeError("Can't calculate count of words in not string value")
    return len(text.split())

def find_unique(lst: list | str) -> list:
    if not isinstance(lst, (list, str)):
        raise TypeError("Your value isn't a list or str")
    return [i for i in lst if lst.count(i) == 1]

def is_palindrome(word: str | list) -> bool:
    if not isinstance(word, (list, str)):
        raise TypeError("Your value isn't a list or str")
    strLen = len(word)
    if strLen % 2 == 0:
        if word[0:(strLen // 2)] == word[(strLen // 2):][::-1]:
            return True
        else:
            return False
    else:
        if word[0:(strLen // 2)] == word[((strLen // 2) + 1):][::-1]:
            return True
        else:
            return False
        
def are_anagrams(word1: str, word2: str) -> bool:
    if not isinstance(word1, str) or not isinstance(word2, str):
        raise TypeError("One of the values aren't str")
    word1 = word1.lower()
    word2 = word2.lower()
    return sorted(list(word1)) == sorted(list(word2))

def combine_dict(dct1: dict, dct2: dict) -> dict:
    if not isinstance(dct1, dict) or not isinstance(dct2, dict):
        raise TypeError("One of the values aren't dict")
    mergedDict = {}
    for key, value in dct1.items():
        mergedDict[key] = value
    for key, value in dct2.items():
        if (
            key in mergedDict
            and isinstance(mergedDict[key], dict)
            and isinstance(value, dict)
        ):
            mergedDict[key] = combine_dict(mergedDict[key], value)
        else:
            mergedDict[key] = value
    return mergedDict