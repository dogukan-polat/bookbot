def count_words(text):
    words = text.split()
    return len(words)

def count_chars(text):
    char_dict = {}
    for char in text:
        char = char.lower()
        if char not in char_dict:
            char_dict[char] = 1
        else:
            char_dict[char] += 1
    return char_dict

def char_list(dict):
    c_list = []
    for key in dict:
        c_list.append({"char": key,
                       "count": dict[key]})
    return c_list