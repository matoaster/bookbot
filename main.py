from stats import get_word_count, count_chars, sort_chars_dict  
import sys 

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    text = read_files(sys.argv[1])
    word_count = get_word_count(text)
    char = count_chars(text)
    sorted_list = sort_chars_dict(char)
    print_report(sys.argv[1], word_count, sorted_list)

def read_files(filepath):
    with open(filepath) as f:
        return f.read()

def print_report(filepath, get_word_count, sorted_list):
    print("========== BOOKBOT ==========")
    print(f"Analyzing book found at {filepath}")
    print("---------- Word Count --------") 
    print(f"Found {get_word_count} total words")
    print("-------- Character Count ------")
    
    for dicts in sorted_list:
        print(f"{dicts['char']}: {dicts['num']}")

main()