def count_characters(strings_list):
    char_count_dict = {}
    for string in strings_list:
        char_count_dict[string] = len(string)
    return char_count_dict

strings_list = ["Aru", "likes", "to", "code" ,"in_python"]

char_count_dict = count_characters(strings_list)

print(char_count_dict)
