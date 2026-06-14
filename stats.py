def get_book_text(file_path:str)->str:
    with open(file_path) as f:
        file_contents = f.read()
        return file_contents

def find_num_words(text:str)->str:
    num_words = text.split()
    return len(num_words)

def find_num_chars(text:str)->str:
    char_count={}
    for char in text.lower():
        char_count[char] = char_count.get(char,0)+1
    return char_count


def sort_on(tuple: tuple[str, int])->int:
    return tuple[1]

def chars_dict_to_sorted_list(char_dict:dict[str,int])->dict[tuple[str,int]]:
    list_of_tuple = []
    # print(char_dict,char_dict.items(),list_of_tuple)
    for char, count in char_dict.items():
        list_of_tuple.append((char,count))

    sorted_list_of_tuple = sorted(list_of_tuple,reverse=True,key=sort_on)
    return sorted_list_of_tuple