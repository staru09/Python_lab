def find_max_number(num1, num2):
    if num1 >= num2:
        return -1
    valid_numbers = []
    for num in range(num1, num2 + 1):
        if 10 <= num <= 99:
            if sum(int(digit) for digit in str(num)) % 3 == 0:
                if num % 5 == 0:
                    valid_numbers.append(num)

    if valid_numbers:
        return max(valid_numbers)
    else:
        return -1

num1 = int(input("Enter the starting number (num1): "))
num2 = int(input("Enter the ending number (num2): "))

max_number = find_max_number(num1, num2)
print(max_number)
