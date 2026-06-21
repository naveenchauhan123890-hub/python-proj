from stats import find_num_words, get_book_text, find_num_chars, chars_dict_to_sorted_list
import sys

def __main__():
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    sys_args = sys.argv
    if len(sys_args) <2:
       print("Usage: python3 main.py <path_to_book>")
       sys.exit(1)
    book_path = sys.argv[1]

    file_contents_present = get_book_text(f"./{book_path}")
    num_words = find_num_words(file_contents_present)
    char_count = find_num_chars(file_contents_present)
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    # for char, count in char_count.items():
    #     print(f"'{char}': {count}")
    print("--------- Character Count -------")
    for tuple in chars_dict_to_sorted_list(char_count):
        if tuple[0] is not " ":
          print(f"{tuple[0]}: {tuple[1]}")
    print("============= END ===============")

__main__()