# Day 2 - Python Fundamentals

Variables, Naming Rules, Data Types, Type Casting, Input/Output, Comments, Basic Syntax, and Practice Programs

Yeh notes beginner learners ke liye simple Hinglish mein banaye gaye hain. Aap isko directly class mein padhkar explain kar sakte ho. Har topic mein pehle simple meaning hai, phir real-life example, phir code, phir output, phir line-by-line explanation.

---

## Day 2 Ka Main Goal

Day 1 mein humne samjha tha ki programming ka matlab computer ko step-by-step instructions dena hota hai. Humne Python ka introduction dekha, first program run kiya, `print()` se output show kiya, `input()` se user se value li, aur variables ka basic taste liya.

Day 2 mein hum Python ke basic building blocks ko detail mein samjhenge. Aaj ke topics hain: variables, variable naming rules, data types, type checking, type casting, input and output handling, comments, basic syntax, and small practice programs.

Simple language mein bolo to aaj hum yeh seekhenge ki Python mein data ko store kaise karte hain, data ka type kaise samajhte hain, user se value kaise lete hain, output clean format mein kaise print karte hain, aur code ko readable kaise banate hain.

---

## Chapter Index - Aaj Kya Kya Seekhoge

| Chapter | Topic | Simple Meaning |
|---|---|---|
| 1 | Variables | Value ko naam dekar store karna |
| 2 | Naming Rules | Variable ka naam sahi tarike se likhna |
| 3 | Data Types | Data kis type ka hai: number, decimal, text, true/false |
| 4 | Type Checking | `type()` se data type check karna |
| 5 | Type Casting | Ek type ko doosre type mein convert karna |
| 6 | Input and Output | User se value lena aur result print karna |
| 7 | Comments | Code ke andar notes likhna |
| 8 | Basic Syntax | Python code likhne ke basic rules |
| 9 | Practical | Student profile and marks calculator |

---

# Chapter 1 - Variables

## Variable Kya Hota Hai?

Variable ek naam wala container hota hai jisme hum value store karte hain. Aap variable ko ek labelled box ki tarah samjho. Box ke upar naam likha hota hai, aur box ke andar value hoti hai.

Real-life example dekho. Agar class mein ek student ka naam, age, city, aur course store karna hai, to hum Python mein variables bana sakte hain.

```python
name = "Rahul"
age = 21
city = "Delhi"
course = "Python"
```

Yahan `name`, `age`, `city`, aur `course` variables hain. In variables ke andar values store hain.

## Code

```python
name = "Rahul"
age = 21
city = "Delhi"
course = "Python"

print(name)
print(age)
print(city)
print(course)
```

## Output

```text
Rahul
21
Delhi
Python
```

## Line-by-Line Explanation

| Line | Code | Explanation |
|---|---|---|
| 1 | `name = "Rahul"` | `name` variable mein text value `Rahul` store ki. |
| 2 | `age = 21` | `age` variable mein number value `21` store ki. |
| 3 | `city = "Delhi"` | `city` variable mein text value `Delhi` store ki. |
| 4 | `course = "Python"` | `course` variable mein text value `Python` store ki. |
| 6 | `print(name)` | `name` variable ki value print hoti hai. |
| 7 | `print(age)` | `age` variable ki value print hoti hai. |

## Teacher Style Explanation

Learners ko aise samjhao:

“Variable ek box hai. Agar box ka naam `name` hai aur uske andar `Rahul` rakha hai, to jab bhi hum `name` print karenge, output mein `Rahul` aayega. Variable ka benefit yeh hai ki value ko baar-baar manually likhne ki zaroorat nahi hoti. Hum value ko ek naam de dete hain aur us naam ko code mein use karte hain.”

---

# Chapter 2 - Variable Naming Rules

## Naming Rules Kyu Important Hain?

Variable ka naam random nahi rakhna chahiye. Python ke kuch rules hote hain. Agar rule follow nahi karoge, to error aayega. Agar naam confusing rakhoge, to code difficult ho jayega.

Good variable names code ko readable banate hain. Jab koi doosra person code padhe, usko samajh aana chahiye ki variable kis value ke liye use ho raha hai.

## Important Rules

| Rule | Correct Example | Wrong Example |
|---|---|---|
| Name letter ya underscore se start ho sakta hai | `student_name` | `1student` |
| Spaces allowed nahi hain | `student_age` | `student age` |
| Special symbols allowed nahi hain | `total_marks` | `total@marks` |
| Python keywords use nahi kar sakte | `student_class` | `class` |
| Names case-sensitive hote hain | `Name` and `name` different hain | Same nahi hain |

## Code

```python
student_name = "Ayesha"
student_age = 20
total_marks = 450

print(student_name)
print(student_age)
print(total_marks)
```

## Output

```text
Ayesha
20
450
```

## Teacher Style Explanation

“Python mein variable names meaningful rakho. Agar aap `x`, `y`, `z` use karoge, code chalega, but samajhna difficult hoga. Agar aap `student_name`, `total_marks`, `daily_hours` use karoge, to code self-explanatory banega. Professional coding mein readable code bahut important hota hai.”

---

# Chapter 3 - Data Types

## Data Type Kya Hota Hai?

Data type batata hai ki value kis kind ki hai. Python ko yeh samajhna hota hai ki value number hai, decimal hai, text hai, ya true/false value hai.

Day 2 mein hum four basic data types samjhenge: `int`, `float`, `str`, and `bool`.

| Data Type | Meaning | Example |
|---|---|---|
| `int` | Whole number | `10`, `21`, `500` |
| `float` | Decimal number | `10.5`, `99.99`, `3.14` |
| `str` | Text/String | `"Rahul"`, `"Python"` |
| `bool` | True/False | `True`, `False` |

## Code

```python
age = 21
price = 99.50
name = "Rahul"
is_student = True

print(age)
print(price)
print(name)
print(is_student)
```

## Output

```text
21
99.5
Rahul
True
```

## Line-by-Line Explanation

| Line | Code | Explanation |
|---|---|---|
| 1 | `age = 21` | `21` whole number hai, iska type `int` hai. |
| 2 | `price = 99.50` | Decimal number hai, iska type `float` hai. |
| 3 | `name = "Rahul"` | Quotes ke andar text hai, iska type `str` hai. |
| 4 | `is_student = True` | True/False value hai, iska type `bool` hai. |

## Teacher Style Explanation

“Data type ko value ka nature samjho. Agar value count karne wali whole number hai, to `int`. Agar decimal hai, to `float`. Agar text hai, to `str`. Agar answer yes/no ya true/false type hai, to `bool`. Python automatically data type detect kar leta hai, lekin programmer ko samajhna zaroori hai.”

---

# Chapter 4 - Type Checking Using `type()`

## `type()` Kya Karta Hai?

`type()` Python ka built-in function hai jo kisi value ya variable ka data type batata hai. Beginner ke liye `type()` bahut useful hai, kyunki isse hum confirm kar sakte hain ki Python value ko kis type ka samajh raha hai.

## Code

```python
age = 21
price = 99.50
name = "Rahul"
is_student = True

print(type(age))
print(type(price))
print(type(name))
print(type(is_student))
```

## Output

```text
<class 'int'>
<class 'float'>
<class 'str'>
<class 'bool'>
```

## Explanation

Yahan `type(age)` output deta hai `<class 'int'>`, kyunki `age` mein whole number store hai. `type(price)` output deta hai `<class 'float'>`, kyunki price decimal number hai. `type(name)` output deta hai `<class 'str'>`, kyunki name text hai. `type(is_student)` output deta hai `<class 'bool'>`, kyunki value `True` hai.

---

# Chapter 5 - Input and Output

## Input Kya Hota Hai?

Input ka matlab user se value lena. Python mein input lene ke liye `input()` function use hota hai. Jab program run hota hai, `input()` user ko message show karta hai aur user keyboard se value type karta hai.

Important baat: `input()` se jo value aati hai, woh by default string hoti hai. Matlab agar user `20` type kare, Python usko text `"20"` ki tarah treat karta hai, number `20` ki tarah nahi.

## Code

```python
name = input("Enter your name: ")
city = input("Enter your city: ")

print("Hello", name)
print("You are from", city)
```

## Output

```text
Enter your name: Rahul
Enter your city: Delhi
Hello Rahul
You are from Delhi
```

## Teacher Style Explanation

“Input user se data lene ka way hai. Real applications mein forms hote hain: name, email, password, city, phone number. Python mein beginner level par hum `input()` se same idea samajhte hain. User jo value type karega, woh variable mein store hogi, phir hum us variable ko program mein use kar sakte hain.”

---

# Chapter 6 - Type Casting

## Type Casting Kya Hota Hai?

Type casting ka matlab ek data type ko doosre data type mein convert karna. Ye especially input ke saath important hai, kyunki `input()` by default string value deta hai.

Agar user se age input lete hain aur us age par calculation karni hai, to age ko `int` mein convert karna padega.

## Problem Without Type Casting

```python
age = input("Enter your age: ")

print(age + 1)
```

Yeh code error dega, kyunki `age` string hai aur hum string mein number add karne ki koshish kar rahe hain.

## Correct Code With Type Casting

```python
age = input("Enter your age: ")
age = int(age)

print("Next year your age will be", age + 1)
```

## Output

```text
Enter your age: 21
Next year your age will be 22
```

## Line-by-Line Explanation

| Line | Code | Explanation |
|---|---|---|
| 1 | `age = input(...)` | User se age input li, but value string form mein aayi. |
| 2 | `age = int(age)` | String age ko integer mein convert kiya. |
| 4 | `age + 1` | Ab calculation possible hai because age number ban chuki hai. |

## Common Casting Functions

| Function | Use |
|---|---|
| `int()` | Value ko whole number mein convert karta hai |
| `float()` | Value ko decimal number mein convert karta hai |
| `str()` | Value ko string/text mein convert karta hai |
| `bool()` | Value ko boolean mein convert karta hai |

---

# Chapter 7 - Comments

## Comment Kya Hota Hai?

Comment code ke andar note hota hai. Python comment ko execute nahi karta. Comment programmer ke liye hota hai, taaki code samajhna easy ho.

Python mein single-line comment ke liye `#` use hota hai.

## Code

```python
# This program prints student details

name = "Rahul"
age = 21

print(name)
print(age)
```

## Explanation

First line comment hai. Python is line ko execute nahi karega. Comment ka use code ka purpose explain karne ke liye hota hai. Beginners ko comments use karne chahiye, but har obvious line par comment nahi likhna chahiye.

---

# Chapter 8 - Basic Python Syntax

## Syntax Kya Hota Hai?

Syntax ka matlab programming language ke writing rules. Jaise English mein grammar hoti hai, waise Python mein syntax hota hai. Agar syntax wrong hai, Python error show karega.

Basic syntax rules:

- Strings quotes mein likhte hain.
- Function call mein brackets use hote hain.
- Variable assignment ke liye `=` use hota hai.
- Python case-sensitive hai.
- Code spelling correct honi chahiye.

## Correct Code

```python
message = "Welcome to Python"
print(message)
```

## Wrong Code

```python
Message = "Welcome to Python"
print(message)
```

Yahan error aa sakta hai, kyunki `Message` aur `message` Python mein different names hain.

---

# Chapter 9 - Practical 1: Student Profile

## Practical Goal

Is practical mein hum user se student details lenge aur clean profile print karenge. Ye practical variables, input, output, and string handling ka practice karayega.

## Code

```python
name = input("Enter student name: ")
age = int(input("Enter age: "))
city = input("Enter city: ")
course = input("Enter course name: ")

print("")
print("Student Profile")
print("----------------")
print("Name:", name)
print("Age:", age)
print("City:", city)
print("Course:", course)
print("Next year age:", age + 1)
```

## Output

```text
Enter student name: Rahul
Enter age: 21
Enter city: Delhi
Enter course name: Python

Student Profile
----------------
Name: Rahul
Age: 21
City: Delhi
Course: Python
Next year age: 22
```

## Detailed Explanation

Yahan `name`, `city`, and `course` string values hain. `age` ko `int()` mein convert kiya gaya hai, kyunki age par calculation karni hai. Last line mein `age + 1` se next year age calculate hoti hai. Is practical se learners ko samajh aata hai ki input by default string hota hai, aur calculation ke liye type casting required hoti hai.

---

# Chapter 10 - Practical 2: Marks Calculator

## Practical Goal

Is practical mein hum three subjects ke marks input lenge, total calculate karenge, percentage calculate karenge, and result print karenge. Ye Day 2 ka most important practical hai.

## Code

```python
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
```

## Output

```text
Enter student name: Ayesha
Enter Math marks: 85
Enter Science marks: 90
Enter English marks: 80

Marks Report
------------
Student: Ayesha
Total Marks: 255.0
Percentage: 85.0
```

## Line-by-Line Explanation

| Line | Code | Explanation |
|---|---|---|
| 1 | `student_name = input(...)` | Student ka naam input liya. |
| 3 | `float(input(...))` | Marks input liye aur decimal number mein convert kiya. |
| 7 | `total_marks = ...` | Three subjects ke marks add kiye. |
| 8 | `percentage = ...` | Percentage formula apply kiya. |
| 12-14 | `print(...)` | Final marks report print ki. |

## Teacher Style Explanation

“Ye practical real-life marksheet ka basic version hai. Agar marks string form mein rahenge, calculation nahi hogi. Isliye hum `float()` use kar rahe hain. Total marks addition se nikalta hai, percentage formula se nikalta hai. Ye small practical future Student Marks Management System project ka base ban sakta hai.”

---

# Chapter 11 - Practical 3: Product Bill Calculator

## Practical Goal

Is practical mein hum user se product name, product price, and quantity input lenge. Phir total bill calculate karenge. Ye practical business billing system ka beginner version hai.

Is practical se learners ko samajh aayega ki real applications mein input values calculation ke liye kaise use hoti hain. Product price decimal ho sakta hai, isliye `float()` use karenge. Quantity whole number hoti hai, isliye `int()` use karenge.

## Code

```python
product_name = input("Enter product name: ")
price = float(input("Enter product price: "))
quantity = int(input("Enter quantity: "))

total_bill = price * quantity

print("")
print("Bill Summary")
print("------------")
print("Product:", product_name)
print("Price:", price)
print("Quantity:", quantity)
print("Total Bill:", total_bill)
```

## Output

```text
Enter product name: Notebook
Enter product price: 45.50
Enter quantity: 4

Bill Summary
------------
Product: Notebook
Price: 45.5
Quantity: 4
Total Bill: 182.0
```

## Line-by-Line Explanation

| Line | Code | Explanation |
|---|---|---|
| 1 | `product_name = input(...)` | Product ka naam user se input liya. Ye string rahega. |
| 2 | `price = float(input(...))` | Product price input liya and decimal number mein convert kiya. |
| 3 | `quantity = int(input(...))` | Quantity input li and whole number mein convert ki. |
| 5 | `total_bill = price * quantity` | Price aur quantity multiply karke bill calculate kiya. |
| 8 | `print("Bill Summary")` | Output ka heading print kiya. |
| 11 | `print("Quantity:", quantity)` | Quantity value print ki. |
| 12 | `print("Total Bill:", total_bill)` | Final bill amount print kiya. |

## Teacher Style Explanation

“Ye practical students ko real-world billing ka idea deta hai. Agar shopkeeper ke paas product price and quantity hai, to total bill multiplication se niklega. Lekin input se price string form mein aata hai, isliye `float()` use karna zaroori hai. Quantity usually whole number hoti hai, isliye `int()` use karte hain. Is practical mein type casting ka real use clear hota hai.”

## Student Modification Task

Is program mein discount add karo. User se discount amount input lo and final bill calculate karo:

```python
final_bill = total_bill - discount
```

---

# Chapter 12 - Practical 4: Age Calculator

## Practical Goal

Is practical mein hum user se birth year and current year input lenge, phir approximate age calculate karenge. Ye type casting and subtraction ka easy real-life practical hai.

## Code

```python
name = input("Enter your name: ")
birth_year = int(input("Enter your birth year: "))
current_year = int(input("Enter current year: "))

age = current_year - birth_year

print("")
print("Age Summary")
print("-----------")
print("Name:", name)
print("Birth Year:", birth_year)
print("Current Year:", current_year)
print("Approx Age:", age)
```

## Output

```text
Enter your name: Rahul
Enter your birth year: 2003
Enter current year: 2026

Age Summary
-----------
Name: Rahul
Birth Year: 2003
Current Year: 2026
Approx Age: 23
```

## Line-by-Line Explanation

| Line | Code | Explanation |
|---|---|---|
| 1 | `name = input(...)` | User ka name input liya. |
| 2 | `birth_year = int(input(...))` | Birth year input liya and integer mein convert kiya. |
| 3 | `current_year = int(input(...))` | Current year input liya and integer mein convert kiya. |
| 5 | `age = current_year - birth_year` | Current year se birth year subtract karke age calculate ki. |
| 8-13 | `print(...)` | Clean age summary print ki. |

## Teacher Style Explanation

“Yahan students ko input, type casting, and calculation ka combined use dikh raha hai. Birth year and current year agar string rahenge to subtraction nahi hogi. Isliye hum dono values ko `int()` mein convert karte hain. Phir simple subtraction se approximate age calculate hoti hai.”

## Student Modification Task

Is program mein city input add karo and final message print karo:

```python
print(name, "from", city, "is approximately", age, "years old.")
```

---

# Chapter 13 - Day 2 Combined Mini Project

## Project Goal

Ab Day 2 ke concepts ko combine karke ek mini project bana sakte hain: Student Learning Summary. Isme learner ka name, age, city, course, daily practice hours, and three subject marks input honge. Program total marks, percentage, and next year age print karega.

## Code

```python
name = input("Enter name: ")
age = int(input("Enter age: "))
city = input("Enter city: ")
course = input("Enter course: ")
daily_hours = float(input("Daily practice hours: "))

python_marks = float(input("Python marks: "))
logic_marks = float(input("Logic marks: "))
project_marks = float(input("Project marks: "))

total = python_marks + logic_marks + project_marks
percentage = (total / 300) * 100

print("")
print("Student Learning Summary")
print("------------------------")
print("Name:", name)
print("Age:", age)
print("Next Year Age:", age + 1)
print("City:", city)
print("Course:", course)
print("Daily Practice:", daily_hours, "hours")
print("Total Marks:", total)
print("Percentage:", percentage)
```

## Teacher Style Explanation

“Ye mini project Day 2 ke saare main concepts combine karta hai. Isme input hai, variables hain, `int()` hai, `float()` hai, addition hai, percentage formula hai, and clean output hai. Agar learner ye project samajh gaya, to Day 2 ka foundation strong hai.”

---

# Day 2 Practice Questions

1. Apna name, age, city, and goal input lo aur clean summary print karo.
2. User se product name, price, and quantity input lo. Total bill calculate karo.
3. User se birth year input lo aur approximate age calculate karo.
4. Three subject marks input lo aur total/percentage calculate karo.
5. Kisi bhi program mein comments add karo and explain karo comments ka use kya hai.
6. Bill calculator mein discount add karo.
7. Age calculator mein city and final sentence add karo.
8. Student Learning Summary mini project complete karo.

---

# Day 2 Summary

Day 2 mein humne variables, naming rules, data types, `type()`, input, output, type casting, comments, and basic syntax samjha. Humne student profile and marks calculator practical bhi kiya.

Important takeaway:

Python mein data ko variable mein store karte hain. Har value ka data type hota hai. User input by default string hota hai. Calculation ke liye type casting zaroori hoti hai. Clean output ke liye `print()` ko properly use karna chahiye.
