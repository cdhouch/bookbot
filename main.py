import sys
from stats import *

def check_args():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    return None

def get_book_text(book):
    with open(book) as f:
        text = f.read()
    return text

def print_results(bpath,wcount,dict):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {bpath}...")
    print("----------- Word Count ----------")
    print(f"Found {wcount} total words")
    print("--------- Character Count -------")
    for key in dict:
        print(f"{key}: {dict[key]}")
    print("============= END ===============")
    return None

def main():
    #check if at least one book is passed in
    check_args()

    book_path = sys.argv[1]
    #frankenstein_path = "books/frankenstein.txt"
    book_text = get_book_text(book_path)
    num_words = count_words(book_text)
    #print(f"{num_words} words found in the document")
    my_dict = symbol_count(book_text)
    sorted_dict_list = dict_to_list(my_dict)
    my_sorted_dict = list_to_dict(sorted_dict_list)
    #print(sorted_dict_list)
    print_results(book_path,num_words,my_sorted_dict)
    return None

if __name__ == "__main__":
    main()