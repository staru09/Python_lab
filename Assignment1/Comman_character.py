def common_characters(str1, str2):
    common_chars = []
    
    for char1 in str1:
        if char1 not in common_chars:
            for char2 in str2:
                if char1 == char2:
                    common_chars.append(char1)
                    break 
    
    unique_common_chars = []
    for char in common_chars:
        if char not in unique_common_chars:
            unique_common_chars.append(char)
    
    if unique_common_chars:
        return ''.join(unique_common_chars)
    else:
        return -1

string1 = input("Enter 1st String")
string2 = input("Enter 2nd String")

result = common_characters(string1, string2)
if result != -1:
    print(f"Common characters: {result}")
else:
    print("No common characters.")
