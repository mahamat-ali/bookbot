def word_count(book_text):
    num_words = len(book_text.split())
    return num_words

def char_count(book_text):
    lower_book_text = book_text.lower().split()
    char_dic = {}
    for word in lower_book_text:
        for char in word:
            if char in char_dic:
                char_dic[char] += 1
            else:
                char_dic[char] = 1
    return char_dic


def sort_on(sorted_char_count):
    return sorted_char_count["num"]


def sorted_char_count(char_count_dic):
    sorted_char_list = []
    for k,v in char_count_dic.items():
        sorted_char_list.append({"char": k, "num": v})
    sorted_char_list.sort(reverse=True, key=sort_on)
    
    return sorted_char_list