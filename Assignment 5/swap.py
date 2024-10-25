def swap_file_content(filename):
    with open(filename, 'r') as file:
        content = file.read()
        mid = len(content) // 2
        swapped_content = content[mid:] + content[:mid]

    with open(filename, 'w') as file:
        file.write(swapped_content)

filename = input("Enter file name: ")
swap_file_content(filename)
print("First and second half swapped.")
