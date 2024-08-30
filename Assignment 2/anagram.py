def check_anagram(str1, str2):
    str1 = str1.lower()
    str2 = str2.lower()

    if len(str1) != len(str2):
        return False
    
    if sorted(str1) != sorted(str2):
        return False

    for i in range(len(str1)):
        if str1[i] == str2[i]:
            return False

    return True

# Test the function
str1 = input("Enter 1st string: ")
str2 = input("Enter 2nd string: ")
print(check_anagram(str1, str2))