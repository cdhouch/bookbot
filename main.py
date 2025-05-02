def get_book_text(book):
    with open(book) as f:
        text = f.read()
    return text

def main():
    frankenstein_path = "books/frankenstein.txt"
    frankentext = get_book_text(frankenstein_path)
    print(frankentext)

if __name__ == "__main__":
    main()