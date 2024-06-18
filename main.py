def main():
    book_path = "books/frankenstein.txt"
    text = get_book(book_path)
    print(f"--- Begin report of {book_path} ---")
    word_count = get_word_count(text)
    print(f"{word_count} words found in the document")
    char_count = get_char_count(text)
    sorted_char_count = sort_char_count(char_count)
    print_sorted_char_count(sorted_char_count)
    print("--- End report ---")

def get_word_count(string):
    words = string.split()
    return len(words)

def get_char_count(text):
    lower_text = text.lower()
    char_count = {}
    for letter in lower_text:
        char_count[letter] = char_count.get(letter, 0) + 1
        #solution recommended by course
        #if letter in char_count:
         #   char_count[letter] += 1
        #else:
         #   char_count.update({letter : 1})
    return char_count

def sort_dict(char_dict):
    #not needed because we're using lambda for our key argument in the sort function
    pass

def sort_char_count(char_dict):
    list_from_dict = list(char_dict.items())
    list_from_dict.sort(reverse=True, key=lambda char: char[1])
    return list_from_dict

def print_sorted_char_count(sorted_list):
    for letter,count in sorted_list:
        if letter.isalpha() == True:
            print(f"The {letter} character was found {count} times")

def get_book(path):
    with open(path) as f:
        return f.read()    

main()

#learnings
#using with for file management
#using .get() to populate a new dictionary
#sort dict to list of tuples
#using lambda as an argument for the built-in sort function
#iterating over two variables (a list of tuples in this case)