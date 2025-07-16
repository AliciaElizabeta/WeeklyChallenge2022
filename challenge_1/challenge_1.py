word1 = 'ab ba'
word2 = 'abba'

def textToSortedList(text):
    return sorted(list(text.replace(" ", "").lower()))

def checkAnagram(word1, word2):
    if (word1 == word2):
        return False
    return textToSortedList(word1) == textToSortedList(word2)


if checkAnagram(word1, word2):
    print("Anagram!")
else:
    print("Not an anagram :(")