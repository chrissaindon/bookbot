def get_word_count(text):
    words = text.split()
    return len(words)

characterDict = {}

def get_character_count(text):
    for word in text:
        word = word.lower()
        for letter in word:
            if letter not in characterDict:
                characterDict[letter] = 1
            else:
                characterDict[letter] += 1
    return characterDict
    
