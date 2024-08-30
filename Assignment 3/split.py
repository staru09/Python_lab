def list_to_string(items):
    if len(items) == 0:
        return ''  
    elif len(items) == 1:
        return items[0]  
    else:
        return ', '.join(items[:-1]) + ', and ' + items[-1]


user_input = input("Enter a list of items separated by commas: ")

items = [item.strip() for item in user_input.split(',')]

result = list_to_string(items)
print(result)
