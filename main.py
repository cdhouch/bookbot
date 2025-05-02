from stats import *

def get_book_text(book):
    with open(book) as f:
        text = f.read()
    return text

def print_results(wcount,dict):
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {wcount} total words")
    print("--------- Character Count -------")
    for key in dict:
        print(f"{key}: {dict[key]}")
    print("============= END ===============")
    return None

def main():
    frankenstein_path = "books/frankenstein.txt"
    frankentext = get_book_text(frankenstein_path)
    num_words = count_words(frankentext)
    #print(f"{num_words} words found in the document")
    my_dict = symbol_count(frankentext)
    sorted_dict_list = dict_to_list(my_dict)
    my_sorted_dict = list_to_dict(sorted_dict_list)
    #print(sorted_dict_list)
    print_results(num_words,my_sorted_dict)
    return None

if __name__ == "__main__":
    main()