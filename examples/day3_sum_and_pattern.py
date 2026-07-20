total = 0

for number in range(1, 11):
    total += number

print("Sum of numbers from 1 to 10 is:", total)

rows = int(input("Enter number of rows: "))

for row in range(1, rows + 1):
    print("*" * row)
