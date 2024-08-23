month_input = input("Enter the month name (e.g., January, JANUARY, january): ").strip().capitalize()
year = int(input("Enter the year: "))

month_names = [
    "January", "February", "March", "April", "May", "June",
    "July", "August", "September", "October", "November", "December"
]

if month_input in month_names:
    month = month_names.index(month_input) + 1
else:
    print("Invalid month name")
    exit()

if month == 2:
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        days = 29
    else:
        days = 28

elif month in [1, 3, 5, 7, 8, 10, 12]:
    days = 31

else:
    days = 30

print(f"{month_input} {year} has {days} days")
