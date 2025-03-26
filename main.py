from stats import count_words
from stats import count_chars
from stats import char_list

def get_book_text(file_path):
    with open(file_path) as f:
        return f.read()

def main():
    path = "books/frankenstein.txt"
    num_words = count_words(get_book_text(path))
    dict_chars = count_chars(get_book_text(path))
    list_chars = char_list(dict_chars)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")
    print("----------- Word Count ----------")
    print(f"{num_words} words found in the document")
    print("--------- Character Count -------")
    for list in list_chars:
        if list["char"].isalpha():
            print(f"{list["char"]}: {list["count"]}")

main()