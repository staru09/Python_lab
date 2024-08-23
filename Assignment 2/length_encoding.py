def run_length_encoding(s):
    if not s:
        return ""

    encoded_string = ""
    count = 1

    for i in range(1, len(s)):
        if s[i] == s[i - 1]:
            count += 1
        else:
            encoded_string += str(count) + s[i - 1]
            count = 1


    encoded_string += str(count) + s[-1]

    return encoded_string

user_input = input("Enter a string with uppercase characters (A-Z): ").strip()


encoded_output = run_length_encoding(user_input)


print("Run-Length Encoded String:", encoded_output)
