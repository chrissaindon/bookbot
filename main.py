from stats import get_word_count
from stats import get_character_count
from stats import sort_dictionary
import sys

def get_book_text(file_path):
    with open(file_path) as book:
       text = book.read()
    return text

def main(file_path):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {file_path}...")
    print("----------- Word Count ----------")
    
    text = get_book_text(file_path)
    num_words = get_word_count(text)
    
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    
    charList = sort_dictionary(get_character_count(text))
    
    for item in charList:
        print(f"{item['char']}: {item['num']}")
    

if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)
else:
    main(sys.argv[1])




        

