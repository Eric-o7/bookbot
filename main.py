def main():
    book_path = "books/frankenstein.txt"
    text = get_book(book_path)
    word_count = get_word_count(text)
    print(f"{get_word_count(text)} words found in the document")
    char_count = get_char_count(text)
    sort_char_count(char_count)

def get_word_count(string):
    words = string.split()
    return len(words)

def get_char_count(text):
    lower_text = text.lower()
    char_count = {}
    for letter in lower_text:
        char_count[letter] = char_count.get(letter, 0) + 1
        #if letter in char_count:
         #   char_count[letter] += 1
        #else:
         #   char_count.update({letter : 1})
    print(char_count)
    return char_count

def sort_char_count(dict):
    pass    

def get_book(path):
    with open(path) as f:
        return f.read()    

main()
