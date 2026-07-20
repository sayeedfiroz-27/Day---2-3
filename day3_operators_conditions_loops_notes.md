# Day 3 - Operators, Conditional Statements, and Loops

Arithmetic Operators, Relational Operators, Logical Operators, Assignment Operators, Membership Operators, Identity Operators, Operator Precedence, Conditions, Loops, Range, Break, Continue, Pass, and Pattern Programs

Yeh notes simple Hinglish mein banaye gaye hain. Aap isko directly classroom mein padhkar explain kar sakte ho. Har topic real-life example, code, output, and explanation ke saath diya gaya hai.

---

## Day 3 Ka Main Goal

Day 2 mein humne variables, data types, input-output, and type casting seekha tha. Ab Day 3 mein hum Python ko decision making aur repetition sikhaenge.

Decision making ka matlab hai condition ke basis par program ka behavior change karna. Example: agar marks 40 se zyada hain to pass, warna fail. Repetition ka matlab hai same kaam ko baar-baar karna. Example: 1 se 10 tak numbers print karna.

Aaj ke topics hain: operators, expression evaluation, if statement, if-else, if-elif-else, nested conditions, for loop, while loop, range function, break, continue, pass, and pattern programs.

---

## Chapter Index - Aaj Kya Kya Seekhoge

| Chapter | Topic | Simple Meaning |
|---|---|---|
| 1 | Arithmetic Operators | Calculation karna |
| 2 | Relational Operators | Comparison karna |
| 3 | Logical Operators | Multiple conditions combine karna |
| 4 | Assignment Operators | Variable update karna |
| 5 | Membership Operators | Value collection mein hai ya nahi |
| 6 | Identity Operators | Same object hai ya nahi |
| 7 | Operator Precedence | Kaunsa operation pehle chalega |
| 8 | if/else | Decision making |
| 9 | Nested Conditions | Condition ke andar condition |
| 10 | for Loop | Fixed repetition |
| 11 | while Loop | Condition-based repetition |
| 12 | break, continue, pass | Loop control |
| 13 | Pattern Programs | Logic building practice |

---

# Chapter 1 - Arithmetic Operators

## Arithmetic Operators Kya Hote Hain?

Arithmetic operators calculations ke liye use hote hain. Jaise addition, subtraction, multiplication, division, remainder, power, and floor division.

## Operators Table

| Operator | Meaning | Example |
|---|---|---|
| `+` | Addition | `10 + 5` |
| `-` | Subtraction | `10 - 5` |
| `*` | Multiplication | `10 * 5` |
| `/` | Division | `10 / 5` |
| `%` | Modulus/Remainder | `10 % 3` |
| `**` | Power | `2 ** 3` |
| `//` | Floor Division | `10 // 3` |

## Code

```python
a = 10
b = 3

print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)
print("Remainder:", a % b)
print("Power:", a ** b)
print("Floor Division:", a // b)
```

## Output

```text
Addition: 13
Subtraction: 7
Multiplication: 30
Division: 3.3333333333333335
Remainder: 1
Power: 1000
Floor Division: 3
```

## Teacher Style Explanation

“Arithmetic operators normal maths jaise hote hain. Difference sirf symbols ka hai. `*` multiplication ke liye use hota hai. `/` normal division deta hai. `%` remainder deta hai, jo even/odd check karne mein useful hota hai. `//` decimal part hata kar floor result deta hai.”

---

# Chapter 2 - Relational Operators

## Relational Operators Kya Hote Hain?

Relational operators comparison karte hain. Inka output hamesha `True` ya `False` hota hai.

| Operator | Meaning |
|---|---|
| `>` | Greater than |
| `<` | Less than |
| `>=` | Greater than or equal |
| `<=` | Less than or equal |
| `==` | Equal to |
| `!=` | Not equal to |

## Code

```python
marks = 75

print(marks > 40)
print(marks == 75)
print(marks != 100)
```

## Output

```text
True
True
True
```

## Explanation

`marks > 40` true hai kyunki 75, 40 se greater hai. `marks == 75` true hai kyunki marks exactly 75 hain. `marks != 100` true hai kyunki marks 100 ke equal nahi hain.

---

# Chapter 3 - Logical Operators

## Logical Operators Kya Hote Hain?

Logical operators multiple conditions ko combine karte hain. Python mein common logical operators hain `and`, `or`, and `not`.

| Operator | Meaning | Example |
|---|---|---|
| `and` | Dono conditions true honi chahiye | age >= 18 and has_id |
| `or` | Koi ek condition true ho to chalega | cash or card |
| `not` | Result reverse karta hai | not logged_in |

## Code

```python
age = 20
has_id = True

print(age >= 18 and has_id == True)
print(age < 18 or has_id == True)
print(not has_id)
```

## Output

```text
True
True
False
```

## Teacher Style Explanation

“Real life mein bhi logical operators use hote hain. Agar movie adult hai, to age 18 se zyada honi chahiye and ID bhi honi chahiye. Agar payment cash ya card se kar sakte ho, to cash available ho or card available ho, dono mein se ek chalega.”

---

# Chapter 4 - Assignment Operators

## Assignment Operators Kya Hote Hain?

Assignment operators variable ki value set ya update karte hain.

## Code

```python
score = 10

score += 5
print(score)

score -= 3
print(score)

score *= 2
print(score)
```

## Output

```text
15
12
24
```

## Explanation

`score += 5` ka matlab hai `score = score + 5`. Isse score 10 se 15 ho gaya. `score -= 3` se score 12 ho gaya. `score *= 2` se score double ho gaya.

---

# Chapter 5 - Membership Operators

## Membership Operators Kya Hote Hain?

Membership operators check karte hain ki koi value kisi collection ke andar present hai ya nahi. Python mein `in` and `not in` use hote hain.

## Code

```python
students = ["Rahul", "Ayesha", "Priya"]

print("Rahul" in students)
print("Aman" in students)
print("Aman" not in students)
```

## Output

```text
True
False
True
```

## Explanation

`"Rahul" in students` true hai kyunki Rahul list mein present hai. `"Aman" in students` false hai kyunki Aman list mein nahi hai.

---

# Chapter 6 - Identity Operators

## Identity Operators Kya Hote Hain?

Identity operators check karte hain ki two variables same object ko refer kar rahe hain ya nahi. Python mein `is` and `is not` use hote hain.

## Code

```python
a = [1, 2, 3]
b = a
c = [1, 2, 3]

print(a is b)
print(a is c)
print(a == c)
```

## Output

```text
True
False
True
```

## Explanation

`a is b` true hai kyunki `b` same list object ko refer kar raha hai. `a is c` false hai kyunki `c` ek alag list object hai. `a == c` true hai kyunki values same hain.

---

# Chapter 7 - Operator Precedence

## Operator Precedence Kya Hota Hai?

Operator precedence batata hai ki expression mein kaunsa operation pehle execute hoga. Maths ki tarah Python mein bhi multiplication addition se pehle hoti hai.

## Code

```python
result = 10 + 5 * 2
print(result)

result2 = (10 + 5) * 2
print(result2)
```

## Output

```text
20
30
```

## Explanation

First expression mein `5 * 2` pehle solve hota hai, phir 10 add hota hai. Isliye result 20 hai. Second expression mein brackets ki wajah se `10 + 5` pehle solve hota hai, phir multiply hota hai. Isliye result 30 hai.

---

# Chapter 8 - Conditional Statements

## Condition Kya Hoti Hai?

Condition decision making ke liye use hoti hai. Agar condition true hai, to ek block execute hota hai. Agar condition false hai, to doosra block execute ho sakta hai.

Real-life example: Agar marks 40 ya usse zyada hain, student pass hai. Warna fail hai.

## if Statement

```python
marks = 75

if marks >= 40:
    print("Pass")
```

## Output

```text
Pass
```

## if-else Statement

```python
marks = 35

if marks >= 40:
    print("Pass")
else:
    print("Fail")
```

## Output

```text
Fail
```

## Line-by-Line Explanation

| Line | Code | Explanation |
|---|---|---|
| 1 | `marks = 35` | Marks variable mein value store ki. |
| 3 | `if marks >= 40:` | Check kiya marks 40 ya zyada hain ya nahi. |
| 4 | `print("Pass")` | Condition true hoti to pass print hota. |
| 5 | `else:` | Agar condition false ho, to else block chalega. |
| 6 | `print("Fail")` | Marks 35 hain, isliye fail print hota hai. |

## Teacher Style Explanation

“Condition program ko decision lene deti hai. Without condition program har time same kaam karega. Condition ke saath program input ke basis par output change kar sakta hai.”

---

# Chapter 9 - if-elif-else

## Multiple Conditions

Jab multiple conditions check karni ho, tab `if-elif-else` use karte hain.

## Code

```python
marks = 82

if marks >= 90:
    print("Grade A")
elif marks >= 75:
    print("Grade B")
elif marks >= 60:
    print("Grade C")
else:
    print("Needs Improvement")
```

## Output

```text
Grade B
```

## Explanation

Python top se conditions check karta hai. Marks 90 se zyada nahi hain, to first condition false. Marks 75 se zyada hain, to second condition true, isliye `Grade B` print hota hai.

---

# Chapter 10 - Nested Conditions

## Nested Condition Kya Hoti Hai?

Nested condition ka matlab condition ke andar condition. Jab decision multiple levels mein ho, tab nested condition use hoti hai.

## Code

```python
age = 20
has_id = True

if age >= 18:
    if has_id:
        print("Entry allowed")
    else:
        print("ID required")
else:
    print("Under age")
```

## Output

```text
Entry allowed
```

## Explanation

Pehle age check hoti hai. Age 18 se zyada hai, to inner condition check hoti hai. `has_id` true hai, isliye entry allowed print hota hai.

---

# Chapter 11 - Loops

## Loop Kya Hota Hai?

Loop ka use same code ko baar-baar run karne ke liye hota hai. Agar hume 1 se 10 tak numbers print karne hain, to 10 baar `print()` likhna bad practice hai. Loop se same kaam short code mein ho jata hai.

---

# Chapter 12 - for Loop and range()

## for Loop Kya Hota Hai?

`for` loop tab use hota hai jab hume pata ho ki loop kitni baar chalana hai. `range()` numbers generate karta hai.

## Code

```python
for number in range(1, 6):
    print(number)
```

## Output

```text
1
2
3
4
5
```

## Explanation

`range(1, 6)` numbers 1 se 5 tak generate karta hai. Ending value 6 include nahi hoti. Har round mein `number` ki value change hoti hai aur print hoti hai.

---

# Chapter 13 - while Loop

## while Loop Kya Hota Hai?

`while` loop tab use hota hai jab loop condition ke basis par chalna ho. Jab tak condition true hai, loop repeat hota rahega.

## Code

```python
count = 1

while count <= 5:
    print(count)
    count += 1
```

## Output

```text
1
2
3
4
5
```

## Explanation

`count` 1 se start hota hai. Jab tak `count <= 5` true hai, loop chalega. Har round mein count print hota hai aur `count += 1` se value increase hoti hai.

---

# Chapter 14 - break, continue, and pass

## Loop Control

`break` loop ko stop karta hai. `continue` current round skip karke next round par jata hai. `pass` kuch nahi karta, bas placeholder ke liye use hota hai.

## break Example

```python
for number in range(1, 10):
    if number == 5:
        break
    print(number)
```

Output:

```text
1
2
3
4
```

## continue Example

```python
for number in range(1, 6):
    if number == 3:
        continue
    print(number)
```

Output:

```text
1
2
4
5
```

## pass Example

```python
for number in range(1, 4):
    pass
```

## Teacher Style Explanation

“Break ka matlab loop se bahar aa jao. Continue ka matlab current step skip karo. Pass ka matlab abhi kuch nahi karna, future mein code add karenge.”

---

# Chapter 15 - Practical 1: Marks Grade System

## Practical Goal

Is practical mein user se marks input lenge, phir condition ke basis par grade print karenge. Ye condition ka best beginner practical hai.

## Code

```python
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
```

## Output

```text
Enter student name: Rahul
Enter marks: 82

Result
------
Student: Rahul
Marks: 82.0
Grade: B
```

## Explanation

Marks ke basis par Python top se conditions check karta hai. Agar marks 90 se zyada hote to grade A hota. Marks 82 hain, to first condition false, second condition true, isliye grade B assign hota hai.

## Deep Line-by-Line Explanation

| Code | Simple Hinglish Explanation |
|---|---|
| `student_name = input("Enter student name: ")` | Student ka naam input liya. Ye output report ko personal banata hai. |
| `marks = float(input("Enter marks: "))` | Marks input liye and `float()` se number mein convert kiye. Marks decimal bhi ho sakte hain, jaise 82.5. |
| `if marks >= 90:` | Python check karta hai kya marks 90 ya usse zyada hain. Agar haan, grade A milega. |
| `grade = "A"` | Agar first condition true hoti, to `grade` variable mein `A` store hota. |
| `elif marks >= 75:` | Agar first condition false hai, Python next condition check karta hai. `elif` ka meaning hai else-if. |
| `grade = "B"` | Agar marks 75 ya usse zyada hain, to grade B assign hota hai. |
| `elif marks >= 60:` | Agar marks 75 se kam hain, tab Python check karta hai kya marks 60 ya usse zyada hain. |
| `elif marks >= 40:` | Ye pass range ke liye condition hai. |
| `else:` | Agar upar ki koi condition true nahi hoti, to else block chalega. |
| `grade = "Fail"` | Agar marks 40 se kam hain, student fail category mein jayega. |
| `print("Result")` | Report ka heading print hota hai. |
| `print("Grade:", grade)` | Jo grade condition ke basis par decide hua, woh final output mein print hota hai. |

## Condition Flow Explanation

Python conditions ko top to bottom check karta hai. Jaise marks 82 hain. Pehle check hota hai `marks >= 90`, ye false hai. Phir check hota hai `marks >= 75`, ye true hai. Jaise hi true condition milti hai, Python us block ko run karta hai and baaki `elif` conditions skip ho jaati hain. Isliye grade B print hota hai.

---

# Chapter 16 - Practical 2: Multiplication Table

## Practical Goal

Is practical mein user se number input lenge aur uska multiplication table print karenge. Ye `for` loop ka strong beginner practical hai.

## Code

```python
number = int(input("Enter a number: "))

for i in range(1, 11):
    print(number, "x", i, "=", number * i)
```

## Output

```text
Enter a number: 5
5 x 1 = 5
5 x 2 = 10
5 x 3 = 15
5 x 4 = 20
5 x 5 = 25
5 x 6 = 30
5 x 7 = 35
5 x 8 = 40
5 x 9 = 45
5 x 10 = 50
```

## Line-by-Line Explanation

| Line | Code | Explanation |
|---|---|---|
| 1 | `number = int(input(...))` | User se number input liya aur integer mein convert kiya. |
| 3 | `for i in range(1, 11):` | Loop 1 se 10 tak chalega. |
| 4 | `number * i` | Har round mein multiplication hoti hai. |

## Deep Line-by-Line Explanation

| Code | Simple Hinglish Explanation |
|---|---|
| `number = int(input("Enter a number: "))` | User se table ka number input liya. Since multiplication karni hai, input ko `int()` se number banaya. |
| `for i in range(1, 11):` | Ye loop `i` ko 1 se 10 tak values deta hai. `range(1, 11)` mein 11 include nahi hota. |
| `print(number, "x", i, "=", number * i)` | Har loop round mein ek table line print hoti hai. Example: agar number 5 and i 3 hai, to output `5 x 3 = 15` hota hai. |

## Loop Dry Run

| Round | `i` Value | Calculation | Output |
|---|---|---|---|
| 1 | 1 | `5 * 1` | `5 x 1 = 5` |
| 2 | 2 | `5 * 2` | `5 x 2 = 10` |
| 3 | 3 | `5 * 3` | `5 x 3 = 15` |
| 10 | 10 | `5 * 10` | `5 x 10 = 50` |

## Teacher Style Explanation

“Loop ka power yahan clearly dikhta hai. Agar loop nahi hota, to hume table ke liye 10 print lines likhni padti. Loop se same logic 10 baar repeat ho raha hai, but code short and clean hai.”

---

# Chapter 17 - Pattern Program

## Pattern Kyu Important Hai?

Pattern programs logic building ke liye useful hote hain. Ye loops ko deeply samajhne mein help karte hain.

## Code

```python
rows = 5

for i in range(1, rows + 1):
    print("*" * i)
```

## Output

```text
*
**
***
****
*****
```

## Explanation

Loop 1 se 5 tak chalta hai. Har row mein `"*" * i` stars repeat karta hai. Jab `i = 1`, one star print hota hai. Jab `i = 5`, five stars print hote hain.

## Deep Line-by-Line Explanation

| Code | Simple Hinglish Explanation |
|---|---|
| `rows = 5` | Pattern mein total rows 5 set ki gayi hain. |
| `for i in range(1, rows + 1):` | Loop 1 se 5 tak chalega. `rows + 1` isliye likha kyunki range ki ending value include nahi hoti. |
| `print("*" * i)` | Python mein string ko number se multiply karne par string repeat hoti hai. Agar `i = 3`, to `"*" * 3` ka output `***` hota hai. |

## Pattern Dry Run

| Row | `i` Value | `"*" * i` | Output |
|---|---|---|---|
| 1 | 1 | `"*" * 1` | `*` |
| 2 | 2 | `"*" * 2` | `**` |
| 3 | 3 | `"*" * 3` | `***` |
| 4 | 4 | `"*" * 4` | `****` |
| 5 | 5 | `"*" * 5` | `*****` |

---

# Chapter 18 - Practical 3: Even or Odd Checker

## Practical Goal

Is practical mein user se ek number input lenge and check karenge ki number even hai ya odd. Ye modulus operator `%` and `if-else` ka best beginner practical hai.

Even number wo hota hai jo 2 se completely divide ho jaye. Agar remainder 0 hai, to number even hai. Agar remainder 0 nahi hai, to number odd hai.

## Code

```python
number = int(input("Enter a number: "))

if number % 2 == 0:
    print(number, "is even")
else:
    print(number, "is odd")
```

## Output 1

```text
Enter a number: 10
10 is even
```

## Output 2

```text
Enter a number: 7
7 is odd
```

## Line-by-Line Explanation

| Line | Code | Explanation |
|---|---|---|
| 1 | `number = int(input(...))` | User se number input liya and integer mein convert kiya. |
| 3 | `number % 2` | Number ko 2 se divide karke remainder check kiya. |
| 3 | `== 0` | Agar remainder 0 hai, condition true hogi. |
| 4 | `print(... "even")` | Condition true hone par even print hoga. |
| 5 | `else:` | Agar condition false ho, else block chalega. |
| 6 | `print(... "odd")` | Number odd print hoga. |

## Teacher Style Explanation

“Even/odd checker se students ko `%` operator ka real use samajh aata hai. Modulus operator remainder deta hai. Agar number ko 2 se divide karne par remainder 0 hai, to number even hai. Ye practical condition and operator dono ko connect karta hai.”

## Extra Detail for Learners

Even/odd logic ka core line ye hai:

```python
if number % 2 == 0:
```

Is line ko tod kar samjho. `number % 2` remainder nikalta hai. `== 0` check karta hai ki remainder zero hai ya nahi. Agar remainder zero hai, condition true. Agar true hai, even print hoga. Agar false hai, else block chalega and odd print hoga.

Examples:

```text
10 % 2 = 0, so 10 even hai
7 % 2 = 1, so 7 odd hai
```

---

# Chapter 19 - Practical 4: Simple Login System

## Practical Goal

Is practical mein user se username and password input lenge. Agar dono correct hain, to login success print hoga. Warna invalid login print hoga.

Ye practical `and` operator and condition ka real-life use dikhata hai.

## Code

```python
username = input("Enter username: ")
password = input("Enter password: ")

if username == "admin" and password == "12345":
    print("Login successful")
else:
    print("Invalid username or password")
```

## Output 1

```text
Enter username: admin
Enter password: 12345
Login successful
```

## Output 2

```text
Enter username: admin
Enter password: 999
Invalid username or password
```

## Line-by-Line Explanation

| Line | Code | Explanation |
|---|---|---|
| 1 | `username = input(...)` | User se username input liya. |
| 2 | `password = input(...)` | User se password input liya. |
| 4 | `username == "admin"` | Username correct hai ya nahi check kiya. |
| 4 | `and` | Dono conditions true honi chahiye. |
| 4 | `password == "12345"` | Password correct hai ya nahi check kiya. |
| 5 | `print("Login successful")` | Dono true hone par success print hota hai. |
| 7 | `print("Invalid...")` | Koi bhi condition false ho, invalid print hota hai. |

## Teacher Style Explanation

“Real apps mein login system username and password dono check karta hai. Sirf username correct hona enough nahi hai, sirf password correct hona bhi enough nahi hai. Dono correct honge tabhi login successful hoga. Isi case mein `and` operator use hota hai.”

## Extra Detail for Learners

Is program ka most important part ye condition hai:

```python
if username == "admin" and password == "12345":
```

Yahan two comparisons ho rahe hain. First comparison username check karta hai. Second comparison password check karta hai. `and` ka rule hai ki dono conditions true honi chahiye. Agar username correct hai but password wrong hai, final result false hoga. Agar password correct hai but username wrong hai, final result false hoga. Dono correct honge tabhi login successful hoga.

## Truth Table

| Username Correct? | Password Correct? | Final Result |
|---|---|---|
| True | True | Login successful |
| True | False | Invalid |
| False | True | Invalid |
| False | False | Invalid |

---

# Chapter 20 - Practical 5: Sum of Numbers Using Loop

## Practical Goal

Is practical mein hum 1 se 10 tak numbers ka sum calculate karenge. Ye `for` loop and assignment operator `+=` ka useful practical hai.

## Code

```python
total = 0

for number in range(1, 11):
    total += number

print("Sum of numbers from 1 to 10 is:", total)
```

## Output

```text
Sum of numbers from 1 to 10 is: 55
```

## Line-by-Line Explanation

| Line | Code | Explanation |
|---|---|---|
| 1 | `total = 0` | Starting mein total zero rakha. |
| 3 | `for number in range(1, 11):` | Number 1 se 10 tak loop mein aayega. |
| 4 | `total += number` | Har number ko total mein add kiya. |
| 6 | `print(...)` | Final sum print kiya. |

## Teacher Style Explanation

“Total variable ko empty basket samjho. Starting mein basket mein 0 hai. Loop har number ko basket mein add karta jaata hai. End mein basket ke andar final sum hota hai.”

## Dry Run Explanation

| Round | `number` | Old `total` | `total += number` ke baad |
|---|---|---|---|
| 1 | 1 | 0 | 1 |
| 2 | 2 | 1 | 3 |
| 3 | 3 | 3 | 6 |
| 4 | 4 | 6 | 10 |
| 5 | 5 | 10 | 15 |
| 10 | 10 | 45 | 55 |

Is dry run se students ko samajh aata hai ki `total` variable har loop round mein update hota ja raha hai. `+=` ka matlab hai old value mein new value add karke same variable mein store karna.

---

# Chapter 21 - Practical 6: User-Controlled Pattern

## Practical Goal

Is practical mein user decide karega ki kitni rows ka star pattern print karna hai. Ye loops and input ka combined practical hai.

## Code

```python
rows = int(input("Enter number of rows: "))

for row in range(1, rows + 1):
    print("*" * row)
```

## Output

```text
Enter number of rows: 4
*
**
***
****
```

## Line-by-Line Explanation

| Line | Code | Explanation |
|---|---|---|
| 1 | `rows = int(input(...))` | User se rows input li and integer mein convert ki. |
| 3 | `range(1, rows + 1)` | Loop 1 se user ke rows number tak chalega. |
| 4 | `"*" * row` | Star ko row number ke according repeat kiya. |

## Teacher Style Explanation

“Pattern programs beginner ke liye thode challenging lag sakte hain, but ye logic building ke liye very useful hain. Har row mein stars ki count increase ho rahi hai. Isi se students ko loop variable ka role samajh aata hai.”

## Extra Detail for Learners

Is code mein user rows decide karta hai. Agar user 4 enter karta hai, loop 1 se 4 tak chalega. Har row mein star count row number ke equal hota hai. Python mein string multiplication possible hai:

```python
"*" * 4
```

Output:

```text
****
```

Yahi reason hai ki pattern program short code mein ban jata hai.

---

# Chapter 22 - Day 3 Combined Mini Project

## Project Goal

Is mini project mein hum Day 3 ke topics combine karenge: input, type casting, conditions, grades, loops, and multiplication table.

Program pehle student ka result grade calculate karega. Phir user se ek number lega and uska multiplication table print karega.

## Code

```python
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
```

## Teacher Style Explanation

“Ye mini project Day 3 ka combined practice hai. Pehla part condition use karta hai grade decide karne ke liye. Second part loop use karta hai multiplication table print karne ke liye. Isse students ko samajh aata hai ki real programs mein multiple concepts ek saath use hote hain.”

## Mini Project Deep Explanation

Is mini project ko two parts mein samjho. First part result system hai. User marks enter karta hai. Python `if-elif-else` chain se grade decide karta hai. Grade ko variable mein store kiya jata hai, phir report mein print kiya jata hai.

Second part multiplication table hai. User ek number enter karta hai. `for` loop `range(1, 11)` ke through 1 se 10 tak repeat hota hai. Har round mein `number * i` calculate hota hai and table line print hoti hai.

Important baat:

```python
grade = "B"
```

Yahan grade print nahi ho raha, sirf store ho raha hai. Later:

```python
print("Grade:", grade)
```

Yahan stored grade output mein show hota hai. Isse students ko samajh aata hai ki variable value ko pehle decide karke baad mein use kar sakte hain.

## Mini Project Improvement Ideas

1. Agar grade Fail ho, to message print karo: “Please practice again.”
2. Agar grade A ho, to message print karo: “Excellent performance.”
3. Table range user se input lo, jaise 1 to 20.
4. Table ke baad even/odd bhi check karo.
5. Final report mein student ka name, grade, and table number print karo.

---

# Day 3 Practice Questions

1. User se age input lo. Agar age 18 ya zyada ho to eligible print karo, warna not eligible.
2. User se number input lo. Check karo number even hai ya odd.
3. User se marks input lo. Grade calculate karo.
4. User se number input lo aur multiplication table print karo.
5. 1 se 100 tak even numbers print karo.
6. 1 se 10 tak sum calculate karo.
7. Star pattern print karo.
8. Password input lo. Agar password correct hai to login success, warna wrong password.
9. User se rows input lo and dynamic pattern print karo.
10. Grade system and multiplication table ko combine karke mini project banao.

---

# Day 3 Summary

Day 3 mein humne operators, conditions, and loops seekhe. Operators calculation and comparison ke liye use hote hain. Conditions program ko decision making deti hain. Loops repeated work ko easy banate hain.

Important takeaway:

Without conditions, program smart decisions nahi le sakta. Without loops, repeated tasks ke liye same code baar-baar likhna padega. Conditions and loops programming logic ke most important building blocks hain.
