from stats import get_num_words, get_char_count

def get_book_text(filepath):
  with open(filepath) as f:
    return f.read()

def main():
  print(f"{get_char_count(get_book_text('books/frankenstein.txt'))} words found in the document")

main()