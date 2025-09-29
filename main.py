from stats import wc
from stats import cc
from stats import sort_by_key_value
import sys

def get_book_text(file_path):
    with open(file_path) as file:
        file_contents = file.read()
        return file_contents

def main():
    if len(sys.argv) == 1:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        file_path = sys.argv[1]
        num_words = wc(get_book_text(file_path))
        my_dict = cc(get_book_text(file_path))
        my_list = sort_by_key_value(my_dict)
        
        print("============ BOOKBOT ============\n")
        print(f"Analyzing book found at {file_path}...\n")
        print("----------- Word Count ----------\n")
        print(f"Found {num_words} total words")
        print("--------- Character Count -------\n")

        index = 0
        for dictionary in my_list:
            print(f"{my_list[index]['char']}: {my_list[index]['num']}")
            index += 1

        print("============= END ===============\n")

main()