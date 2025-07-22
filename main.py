from stats import get_num_words, get_char_count, get_sorted_dictionaries
from sys import argv, exit

if len(argv) < 2:
    print("Usage: python3 main.py <path_to_book>")
    exit(1)

def get_book_text(filepath):
  with open(filepath) as f:
    return f.read()
  

num_words = get_num_words(get_book_text(argv[1]))
char_count = get_char_count(get_book_text(argv[1]))
sorted_dictionaries = get_sorted_dictionaries(char_count)

def main():
  print(argv)
  print("============ BOOKBOT ============")
  print("Analyzing book found at books/frankenstein.txt")
  print("----------- Word Count ----------")
  print(f"Found {num_words} total words")
  print("--------- Character Count -------")
  for item in sorted_dictionaries:
    if item["char"].isalpha():
      print(f"{item['char']}: {item['num']}")
  print("============= END ===============")


main()