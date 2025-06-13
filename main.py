import sys
from curses.ascii import isalpha

from stats import get_num_words, get_character_count, organise_character_count


def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
        return file_contents


def main():
    print("============ BOOKBOT ============")
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    url = sys.argv[1]
    file_contents = get_book_text(url)
    print("Analyzing book found at books/frankenstein.txt...")
    word_count = get_num_words(file_contents)
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    character_count = get_character_count(file_contents)
    organised = organise_character_count(character_count)
    for item in organised:
        if not isalpha(item["char"]):
            continue
        print(f"{item["char"]}: {item["num"]}")
    print("============= END ===============")


main()