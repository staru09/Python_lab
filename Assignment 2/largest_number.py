from functools import cmp_to_key

def compare(a, b):
    if a + b > b + a:
        return -1
    elif a + b < b + a:
        return 1
    else:
        return 0

def create_largest_number(numbers):
    numbers_str = list(map(str, numbers))
    
    sorted_numbers = sorted(numbers_str, key=cmp_to_key(compare))
    
    largest_number = ''.join(sorted_numbers)
    
    return largest_number

numbers_input = input("Enter a list of two-digit numbers (separated by commas): ").strip()
numbers_list = list(map(int, numbers_input.split(',')))

largest_number = create_largest_number(numbers_list)

print("Largest possible number:", largest_number)
