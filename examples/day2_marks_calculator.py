student_name = input("Enter student name: ")

math_marks = float(input("Enter Math marks: "))
science_marks = float(input("Enter Science marks: "))
english_marks = float(input("Enter English marks: "))

total_marks = math_marks + science_marks + english_marks
percentage = (total_marks / 300) * 100

print("")
print("Marks Report")
print("------------")
print("Student:", student_name)
print("Total Marks:", total_marks)
print("Percentage:", percentage)
