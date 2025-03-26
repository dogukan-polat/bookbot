from stats import count_words
from stats import count_chars
from stats import char_list
import sys

def get_book_text(file_path):
    with open(file_path) as f:
        return f.read()

def sort_by_count(dict):
    return dict["count"]

def main():
    print("============ BOOKBOT ============")
    #if len(sys.argv) != 2:
    #    print("Usage: python3 main.py <path_to_book>")
    #    sys.exit(1)
    try:
        path = sys.argv[1]
    except Exception as e:
         print(e)
         print("Usage: python3 main.py <path_to_book>")
         sys.exit(1)
    try:
        num_words = count_words(get_book_text(path))
    except Exception as e:
        print(e)
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    dict_chars = count_chars(get_book_text(path))
    list_chars = char_list(dict_chars)
    list_chars.sort(reverse=True, key=sort_by_count)
    print(f"Analyzing book found at {path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for list in list_chars:
        if list["char"].isalpha():
            print(f"{list["char"]}: {list["count"]}")
    print("============= END ===============")

main()