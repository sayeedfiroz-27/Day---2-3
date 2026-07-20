student_name = input("Enter student name: ")
marks = float(input("Enter marks: "))

if marks >= 90:
    grade = "A"
elif marks >= 75:
    grade = "B"
elif marks >= 60:
    grade = "C"
elif marks >= 40:
    grade = "D"
else:
    grade = "Fail"

print("")
print("Result")
print("------")
print("Student:", student_name)
print("Marks:", marks)
print("Grade:", grade)

number = int(input("Enter a number for multiplication table: "))

for i in range(1, 11):
    print(number, "x", i, "=", number * i)
