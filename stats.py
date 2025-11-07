def get_word_count(text):
    words = text.split()
    return len(words)

def get_character_count(text):
    characterDict = {}
    for word in text:
        word = word.lower()
        for letter in word:
            if letter not in characterDict:
                characterDict[letter] = 1
            else:
                characterDict[letter] += 1
    return characterDict



def sort_on(countList):
    return countList["num"]


def sort_dictionary(characterDict):
    countList = []
    for character, num in characterDict.items():
        if not character.isalpha():
            continue
        countList.append({"char" : character,
                    "num"  : num
})
    countList.sort(reverse=True, key=sort_on)
    return countList
        

    
