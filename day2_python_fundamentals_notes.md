# Day 2 - Python Fundamentals

## Topics Covered

Variables in Python, Naming Rules, Data Types, Type Casting, Input and Output Handling, Comments in Python, Basic Python Syntax, and Basic Programming Practice.

Yeh document fresh format mein banaya gaya hai. Har topic ko individually explain kiya gaya hai. Pehle topic ka meaning hai, phir kyu use karte hain, kya fayda hai, phir practical code, output, aur uske baad har code line ka simple Hinglish explanation diya gaya hai.

---

# 1. Variables in Python

## Topic Samjho

Variable Python mein ek named container hota hai jisme hum data store karte hain. Simple language mein variable ek dabba hai jiske upar naam likha hota hai. Us dabbe ke andar value rakhi hoti hai. Jaise `name` dabbe ke andar `"Rahul"` rakha ho sakta hai, aur `age` dabbe ke andar `21` rakha ho sakta hai.

## Kyu Use Karte Hain?

Variables isliye use karte hain kyunki program mein values ko baar-baar use karna hota hai. Agar value ko ek naam de diya, to hum us naam ko code mein kahin bhi use kar sakte hain. Isse code clean, readable, aur manageable banta hai.

## Fayda

Variables se data store karna easy hota hai. Agar value change karni ho to ek jagah change kar sakte hain. Real applications mein user name, price, marks, email, city, password, total amount, percentage jaise data variables mein hi store hote hain.

## Practical Code

```python
student_name = "Rahul"
student_age = 21
course_name = "Python"

print(student_name)
print(student_age)
print(course_name)
```

## Output

```text
Rahul
21
Python
```

## Detailed Code Explanation

| Line | Code | Explanation |
|---|---|---|
| 1 | `student_name = "Rahul"` | Is line mein `student_name` naam ka variable banaya gaya hai. Is variable ke andar `"Rahul"` text value store ki gayi hai. Quotes batate hain ki value string/text hai. Jab bhi hum `student_name` print karenge, Python uske andar stored value `Rahul` show karega. |
| 2 | `student_age = 21` | Is line mein `student_age` variable banaya gaya hai. Iske andar number `21` store hai. Yahan quotes nahi hain kyunki age number hai. Agar future mein age par calculation karni ho, to number form useful hota hai. |
| 3 | `course_name = "Python"` | Is line mein course ka naam store kiya gaya hai. `course_name` meaningful variable name hai, isliye code padhte hi samajh aa jata hai ki isme course ka naam hai. Text value quotes mein likhi gayi hai. |
| 5 | `print(student_name)` | Ye line `student_name` variable ki value screen par print karti hai. Yahan quotes nahi lagaye kyunki hume word `student_name` print nahi karna, balki us variable ke andar jo value hai woh print karni hai. |
| 6 | `print(student_age)` | Ye line age variable ki value print karti hai. Output mein `21` aata hai. Print function variable ke andar stored value ko terminal par show karta hai. |
| 7 | `print(course_name)` | Ye line course name print karti hai. Since `course_name` mein `"Python"` store hai, output `Python` hota hai. |

---

# 2. Naming Rules

## Topic Samjho

Naming rules ka matlab hai Python mein variable ka naam kaise likhna chahiye. Variable ka naam random ya invalid nahi hona chahiye. Python kuch names accept karta hai aur kuch names par error deta hai.

## Kyu Use Karte Hain?

Naming rules follow karna zaroori hai kyunki agar variable name invalid hua to program run hi nahi hoga. Meaningful names use karne se code padhna easy hota hai. Professional coding mein readable names bahut important hote hain.

## Fayda

Good variable names se code self-explanatory hota hai. Example: `total_marks` dekhte hi samajh aata hai ki isme marks ka total hai. Agar hum sirf `x` likhen, to beginner ko samajh nahi aayega ki variable ka purpose kya hai.

## Practical Code

```python
student_name = "Ayesha"
student_city = "Delhi"
total_marks = 450

print(student_name)
print(student_city)
print(total_marks)
```

## Output

```text
Ayesha
Delhi
450
```

## Detailed Code Explanation

| Line | Code | Explanation |
|---|---|---|
| 1 | `student_name = "Ayesha"` | `student_name` valid variable name hai kyunki isme space nahi hai. Space ki jagah underscore `_` use hua hai. Is variable mein student ka naam store hai. Ye naam readable hai, isliye purpose clear hai. |
| 2 | `student_city = "Delhi"` | Ye variable student ki city store karta hai. Naam meaningful hai, isliye code padhne wale ko samajh aata hai ki yeh city ke liye hai. Text value quotes mein hai. |
| 3 | `total_marks = 450` | Is variable mein marks ka total store hai. Variable number se start nahi ho raha, isliye valid hai. Value number hai, isliye quotes nahi lagaye gaye. |
| 5 | `print(student_name)` | Student name variable ki value print hoti hai. Output `Ayesha` aata hai. |
| 6 | `print(student_city)` | City variable ki value print hoti hai. Output `Delhi` aata hai. |
| 7 | `print(total_marks)` | Total marks print hote hain. Output `450` aata hai. |

---

# 3. Data Types (int, float, str, bool)

## Topic Samjho

Data type batata hai ki value kis type ki hai. Python mein common data types hain `int`, `float`, `str`, and `bool`. `int` whole number ke liye, `float` decimal number ke liye, `str` text ke liye, aur `bool` True/False ke liye use hota hai.

## Kyu Use Karte Hain?

Data types isliye important hain kyunki Python ko pata hona chahiye ki value ke saath kya operation possible hai. Number par calculation hoti hai, text par string operations hote hain, aur boolean values conditions mein use hoti hain.

## Fayda

Data types samajhne se errors kam hote hain. Agar aapko pata hai input string hota hai, to calculation se pehle type casting karoge. Agar value text hai, to quotes use karoge. Isse code sahi chalega.

## Practical Code

```python
age = 21
percentage = 85.5
name = "Rahul"
is_pass = True

print(type(age))
print(type(percentage))
print(type(name))
print(type(is_pass))
```

## Output

```text
<class 'int'>
<class 'float'>
<class 'str'>
<class 'bool'>
```

## Detailed Code Explanation

| Line | Code | Explanation |
|---|---|---|
| 1 | `age = 21` | `age` variable mein whole number store hai. Whole number ka data type `int` hota hai. Age, quantity, count jaise values usually integer hoti hain. |
| 2 | `percentage = 85.5` | Percentage decimal value hai. Decimal number ka data type `float` hota hai. Marks percentage, price, temperature jaise values float ho sakti hain. |
| 3 | `name = "Rahul"` | Name text value hai, isliye quotes mein likha gaya hai. Text ka data type `str` hota hai. `str` ka full form string hai. |
| 4 | `is_pass = True` | `True` boolean value hai. Boolean ka data type `bool` hota hai. Conditions mein `True` and `False` values bahut useful hoti hain. |
| 6 | `print(type(age))` | `type(age)` Python se poochta hai ki age ka data type kya hai. `print()` us type ko screen par show karta hai. Output `<class 'int'>` hota hai. |
| 7 | `print(type(percentage))` | Ye line percentage variable ka type check karti hai. Since value decimal hai, output `<class 'float'>` hota hai. |
| 8 | `print(type(name))` | Ye line name variable ka type check karti hai. Since name text hai, output `<class 'str'>` hota hai. |
| 9 | `print(type(is_pass))` | Ye line boolean variable ka type check karti hai. Since value `True` hai, output `<class 'bool'>` hota hai. |

---

# 4. Type Casting

## Topic Samjho

Type casting ka matlab hota hai ek data type ko doosre data type mein convert karna. Example: string `"21"` ko integer `21` mein convert karna. Python mein `int()`, `float()`, `str()`, and `bool()` casting ke liye use hote hain.

## Kyu Use Karte Hain?

Type casting mostly input ke saath use hoti hai. `input()` function user se value string form mein leta hai. Agar hume calculation karni hai, to us string ko number mein convert karna padta hai.

## Fayda

Type casting se calculations possible hoti hain. Agar user age ya marks enter karta hai, woh pehle string hota hai. `int()` ya `float()` se convert karne ke baad hi addition, subtraction, percentage, bill calculation possible hota hai.

## Practical Code

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

## Detailed Code Explanation

| Line | Code | Explanation |
|---|---|---|
| 1 | `age = input("Enter your age: ")` | Ye line user se age input leti hai. `input()` ke andar jo message hai woh user ko screen par dikhta hai. User jo value type karta hai woh `age` variable mein store hoti hai. Important: yeh value abhi string form mein hoti hai. |
| 2 | `age = int(age)` | Is line mein string age ko integer mein convert kiya gaya hai. Right side wala `int(age)` old string value ko number banata hai. Left side wala `age` same variable ko updated integer value ke saath store karta hai. |
| 4 | `print("Next year your age will be", age + 1)` | Ab age number ban chuki hai, isliye `age + 1` calculation possible hai. Python next year age calculate karta hai. Print function sentence aur result ko ek saath show karta hai. |

---

# 5. Input and Output Handling

## Topic Samjho

Input ka matlab user se data lena. Output ka matlab screen par result show karna. Python mein input ke liye `input()` and output ke liye `print()` use hota hai.

## Kyu Use Karte Hain?

Real programs user ke data par kaam karte hain. Jaise name, city, marks, price, password user enter karta hai. Program us data ko process karta hai and output show karta hai.

## Fayda

Input-output se program interactive banta hai. Program fixed nahi rehta. Har user apni value enter kar sakta hai aur output uske according change hota hai.

## Practical Code

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

## Detailed Code Explanation

| Line | Code | Explanation |
|---|---|---|
| 1 | `name = input("Enter your name: ")` | Program user se name poochta hai. User jo naam type karega woh `name` variable mein store hoga. Prompt clear hai, isliye user ko pata hai kya enter karna hai. |
| 2 | `city = input("Enter your city: ")` | Program user se city poochta hai. City bhi text value hoti hai, isliye direct input store kar sakte hain. |
| 4 | `print("Hello", name)` | Ye line greeting print karti hai. Fixed text `"Hello"` and variable `name` ek saath print hote hain. Comma automatically space add karta hai. |
| 5 | `print("You are from", city)` | Ye line user ki city ke saath sentence print karti hai. Output user input ke according change hota hai. |

---

# 6. Comments in Python

## Topic Samjho

Comment code ke andar note hota hai. Python comment ko execute nahi karta. Comment ka use code explain karne ke liye hota hai.

## Kyu Use Karte Hain?

Comments isliye use karte hain taaki future mein code samajhna easy ho. Jab code bada hota hai, comments help karte hain ki kaunsa part kis kaam ke liye hai.

## Fayda

Comments se code readable hota hai. Team project mein doosre developers ko bhi code ka purpose samajh aata hai. Beginners ke liye comments revision mein help karte hain.

## Practical Code

```python
# This program prints student details

name = "Ayesha"
course = "Python"

print(name)
print(course)
```

## Output

```text
Ayesha
Python
```

## Detailed Code Explanation

| Line | Code | Explanation |
|---|---|---|
| 1 | `# This program prints student details` | Ye comment line hai. Python is line ko execute nahi karta. Ye sirf human reader ko batata hai ki program student details print karega. |
| 3 | `name = "Ayesha"` | Is line mein name variable create hota hai. Comment ke baad actual executable code start hota hai. |
| 4 | `course = "Python"` | Course variable mein Python text store hota hai. Ye value later output mein print hogi. |
| 6 | `print(name)` | Name variable ki value print hoti hai. Output `Ayesha` hota hai. |
| 7 | `print(course)` | Course variable ki value print hoti hai. Output `Python` hota hai. |

---

# 7. Basic Python Syntax

## Topic Samjho

Syntax ka matlab programming language ke writing rules. Jaise English mein grammar hoti hai, waise Python mein syntax hota hai. Agar syntax wrong hua to error aayega.

## Kyu Use Karte Hain?

Syntax rules follow karne se Python code samajh paata hai. Quotes, brackets, indentation, colon, spelling, case sensitivity sab syntax ka part hain.

## Fayda

Syntax clear hone se beginner errors kam hote hain. Student ko pata hota hai string quotes mein likhni hai, function brackets ke saath call hota hai, aur Python case-sensitive hota hai.

## Practical Code

```python
message = "Welcome to Python"
print(message)
```

## Output

```text
Welcome to Python
```

## Detailed Code Explanation

| Line | Code | Explanation |
|---|---|---|
| 1 | `message = "Welcome to Python"` | `message` variable mein text store kiya gaya hai. Text quotes ke andar hai, isliye Python ise string samajhta hai. Assignment ke liye single `=` use hota hai. |
| 2 | `print(message)` | Ye line `message` variable ki stored value print karti hai. Yahan quotes nahi lagaye because hume variable ki value chahiye. Output `Welcome to Python` hota hai. |

---

# 8. Basic Programming Practice

## Topic Samjho

Basic programming practice ka matlab hai chhote-chhote programs likhkar concepts apply karna. Sirf theory padhne se programming strong nahi hoti. Code type karna, run karna, error solve karna zaroori hai.

## Kyu Use Karte Hain?

Practice se learner ko confidence milta hai. Variables, input, output, type casting, comments, syntax sab ek saath use karna aata hai.

## Fayda

Practice programs future projects ka base banate hain. Student profile, bill calculator, marks calculator jaise programs se real-life logic samajh aata hai.

## Practical Code

```python
student_name = input("Enter student name: ")
marks = float(input("Enter marks: "))

print("")
print("Student Result")
print("Name:", student_name)
print("Marks:", marks)
```

## Output

```text
Enter student name: Rahul
Enter marks: 88

Student Result
Name: Rahul
Marks: 88.0
```

## Detailed Code Explanation

| Line | Code | Explanation |
|---|---|---|
| 1 | `student_name = input("Enter student name: ")` | User se student name input liya ja raha hai. Naam string hota hai, isliye direct input store kar sakte hain. |
| 2 | `marks = float(input("Enter marks: "))` | Marks input liye ja rahe hain. Since marks decimal bhi ho sakte hain, `float()` use karke input ko number mein convert kiya gaya. |
| 4 | `print("")` | Ye blank line print karta hai. Output ko clean and readable banane ke liye blank line useful hoti hai. |
| 5 | `print("Student Result")` | Ye output ka heading print karta hai. Heading se user ko samajh aata hai ki result section start ho gaya hai. |
| 6 | `print("Name:", student_name)` | Student ka naam label ke saath print hota hai. Comma text and variable ko combine karta hai. |
| 7 | `print("Marks:", marks)` | Marks variable ki value print hoti hai. Since marks float mein convert hue hain, output `88.0` aa sakta hai. |

