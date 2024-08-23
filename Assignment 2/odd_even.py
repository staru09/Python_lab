def odd():
    return [num for num in sample_data if num % 2 != 0]

def even():
    return [num for num in sample_data if num % 2 == 0]

def sum_of_numbers(data, func=None):
    if func:
        return sum(func())
    else:
        return sum(data)

sample_data = range(1, 11)

print("Odd numbers:", odd())             
print("Even numbers:", even())             

print("Sum of all numbers:", sum_of_numbers(sample_data))       
print("Sum of odd numbers:", sum_of_numbers(sample_data, odd))      
print("Sum of even numbers:", sum_of_numbers(sample_data, even))       
