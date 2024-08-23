import random

def find_more_than_average(marks):
    average_mark = sum(marks) / len(marks)
    count = 0
    for mark in marks:
        if mark > average_mark:
            count += 1
    percentage = (count / len(marks)) * 100
    return percentage

def generate_frequency(marks):
    frequency = [0] * 26 
    for mark in marks:
        frequency[mark] += 1
    return frequency

def sort_marks(marks):
    return sorted(marks)

marks = tuple(random.randint(0, 25) for _ in range(10))

print("Marks of students:", marks)

more_than_average = find_more_than_average(marks)
print(f"Percentage of students scoring more than average: {more_than_average:.2f}%")

frequency = generate_frequency(marks)
print("Frequency of each mark (0-25):", frequency)

sorted_marks = sort_marks(marks)
print("Sorted marks:", sorted_marks)
