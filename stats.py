def get_word_count(text):
    words = text.split()
    word_count = len(words)
    return word_count

def count_chars(text):
    chars = {}
    lowered_contents = text.lower()

    for char in lowered_contents:
        if char in chars:
            chars[char] += 1
        else:
            chars[char] = 1

    return chars
    
def sort_on(items):
    return items["num"]

def sort_chars_dict(num_chars_dictionary):

    dict_list = []
    for ch in num_chars_dictionary:
        dict_list.append({"char" : ch ,"num" : num_chars_dictionary[ch]})
    dict_list.sort(reverse=True, key=sort_on)
    return dict_list

