from stats import get_word_count
from stats import get_character_count

def get_book_text(file_path):
    with open(file_path) as book:
       text = book.read()
    return text


def main(file_path):
    num_words = get_word_count(get_book_text(file_path))
    print(f"Found {num_words} total words")
    characters = get_character_count(get_book_text(file_path))
    print(characters)
   

main("books/frankenstein.txt")



        

