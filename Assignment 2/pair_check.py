def find_pairs_of_numbers(numbers, target_sum):
    count = 0
    seen_numbers = set()

    for number in numbers:
        complement = target_sum - number
        if complement in seen_numbers:
            count += 1
        seen_numbers.add(number)

    return count


numbers_input = input("Enter a list of positive integers (separated by commas): ").strip()
numbers_list = list(map(int, numbers_input.split(',')))
target_sum = int(input("Enter the target sum: "))


pair_count = find_pairs_of_numbers(numbers_list, target_sum)

print(f"Number of pairs that add up to {target_sum}: {pair_count}")
