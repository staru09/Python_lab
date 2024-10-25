def mad_libs(filename):
    with open(filename, 'r') as file:
        content = file.read()

    replacements = {'ADJECTIVE': 'an adjective', 'NOUN': 'a noun', 'VERB': 'a verb', 'ADVERB': 'an adverb'}
    user_inputs = {}

    for key in replacements:
        user_input = input(f"Enter {replacements[key]}: ")
        user_inputs[key] = user_input

    for key, user_input in user_inputs.items():
        content = content.replace(key, user_input)

    print("\nGenerated story:")
    print(content)

filename = input("Enter the file name for Mad Libs: ")
mad_libs(filename)
