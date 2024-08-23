m = int(input("Enter the size of pattern :"))    
for i in range(1, m + 1):
    for j in range(1, i + 1):
        print(j, end=' ')
    print()

for i in range(m - 1, 0, -1):
    for j in range(1, i + 1):
        print(j, end=' ')
    print()  