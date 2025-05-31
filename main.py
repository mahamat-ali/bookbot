import sys
from stats import word_count, char_count, sorted_char_count

def get_book_text(filePath):
    with open(filePath) as f:
        book_text = f.read()
        return book_text


def main():

    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book_text = get_book_text(sys.argv[1])
    word_c = word_count(book_text)
    char_c = char_count(book_text)
   

    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {word_c} total words")
    print("--------- Character Count -------")
    for dic in sorted_char_count(char_c):
        print(f"{dic['char']}: {dic['num']}")
    print("============= END ===============")

main()
