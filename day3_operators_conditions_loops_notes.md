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

# Day 3 Keyword Master Guide - Pehle Yeh Clear Karo

Day 3 mein kuch keywords aur symbols baar-baar use honge. Agar yeh keywords clear ho gaye, to operators, conditions, loops, and patterns samajhna easy ho jayega. Is section ko class ke start mein zaroor explain karo.

## `if` Keyword

`if` ka meaning hota hai “agar”. Python mein `if` decision making ke liye use hota hai. Jab hume program se puchna ho ki koi condition true hai ya false, tab `if` use karte hain. Example: agar marks 40 se zyada hain, to pass print karo.

`if` ke baad condition likhi jaati hai. Condition ka result `True` ya `False` hota hai. Agar condition true hoti hai, to `if` ke andar wala indented code run hota hai. Agar condition false hoti hai, to Python us block ko skip kar deta hai.

```python
marks = 75

if marks >= 40:
    print("Pass")
```

Line `if marks >= 40:` mein Python check karta hai ki marks 40 ya usse zyada hain ya nahi. Colon `:` batata hai ki condition ka block ab start hoga. Next line mein indentation hai, isliye `print("Pass")` if block ka part hai.

## `else` Keyword

`else` ka meaning hota hai “warna”. Jab `if` condition false ho jaati hai, tab `else` block run hota hai. `else` ke saath condition nahi likhte, kyunki else ka kaam hi hota hai false case handle karna.

```python
marks = 35

if marks >= 40:
    print("Pass")
else:
    print("Fail")
```

Yahan marks 35 hain, so `marks >= 40` false hai. Python `print("Pass")` ko skip karega and `else` block mein jayega. `else` block ke andar `print("Fail")` run hoga. Isse program two possible outputs handle kar sakta hai.

## `elif` Keyword

`elif` ka full meaning hota hai “else if”. Jab hume multiple conditions check karni hoti hain, tab `elif` use hota hai. Python conditions ko top se bottom check karta hai. Jis condition par first time true milta hai, uska block run hota hai and baaki conditions skip ho jaati hain.

```python
marks = 82

if marks >= 90:
    print("Grade A")
elif marks >= 75:
    print("Grade B")
else:
    print("Needs Improvement")
```

Yahan Python pehle check karta hai marks 90 ya usse zyada hain kya. Ye false hai. Phir Python `elif marks >= 75` check karta hai. Ye true hai, so `Grade B` print hota hai. Iske baad Python `else` tak nahi jaata.

## `for` Keyword

`for` loop fixed repetition ke liye use hota hai. Jab hume pata ho ki code kitni baar repeat karna hai, tab `for` loop best hota hai. Example: 1 se 10 tak numbers print karna, table print karna, list ke items print karna.

```python
for number in range(1, 6):
    print(number)
```

Is code mein `range(1, 6)` numbers 1 se 5 tak generate karta hai. `number` loop variable hai. Har round mein `number` ki value change hoti hai. Pehle 1, phir 2, phir 3, phir 4, phir 5. Har round mein `print(number)` run hota hai.

## `while` Keyword

`while` loop condition-based repetition ke liye use hota hai. Jab tak condition true hoti hai, loop repeat hota rehta hai. Agar condition false ho jaati hai, loop stop ho jata hai.

```python
count = 1

while count <= 5:
    print(count)
    count += 1
```

Yahan `count` 1 se start hota hai. Jab tak `count <= 5` true hai, loop chalega. Har round mein count print hota hai and `count += 1` se count increase hota hai. Agar `count += 1` nahi likhenge, loop infinite ho sakta hai.

## `range()` Function

`range()` numbers generate karta hai. Ye mostly `for` loop ke saath use hota hai. Important rule: range ki ending value include nahi hoti.

```python
range(1, 6)
```

Ye 1, 2, 3, 4, 5 generate karega. 6 include nahi hoga. Agar hume 1 se 10 tak chalana hai, to `range(1, 11)` likhna padega. Beginners aksar yahan confuse hote hain, isliye ending value ka rule baar-baar explain karo.

## `break` Keyword

`break` loop ko turant stop karta hai. Agar loop ke beech mein koi condition true ho jaye aur hume loop continue nahi karna, tab `break` use karte hain.

```python
for number in range(1, 10):
    if number == 5:
        break
    print(number)
```

Jab number 5 hota hai, `break` execute hota hai and loop stop ho jata hai. Isliye output mein 1, 2, 3, 4 print hote hain, but 5 print nahi hota. Break ka meaning hai: “ab loop se bahar nikal jao”.

## `continue` Keyword

`continue` loop ko stop nahi karta. Ye sirf current round skip karta hai and next round par chala jata hai. Jab kisi specific value ko ignore karna ho, tab continue useful hota hai.

```python
for number in range(1, 6):
    if number == 3:
        continue
    print(number)
```

Yahan jab number 3 hota hai, `continue` run hota hai. Us round mein `print(number)` execute nahi hota. Output 1, 2, 4, 5 aata hai. Continue ka meaning hai: “is round ko skip karo, next round par jao”.

## `pass` Keyword

`pass` ka matlab hai “abhi kuch nahi karna”. Python empty block allow nahi karta. Agar hume future mein code add karna hai but abhi block empty rakhna hai, tab `pass` use karte hain.

```python
for number in range(1, 4):
    pass
```

Ye code koi output nahi dega, but error bhi nahi dega. `pass` placeholder hai. Isse Python ko pata chalta hai ki block intentionally empty hai.

## Colon `:` ka Role

Python mein `if`, `elif`, `else`, `for`, and `while` ke baad colon `:` lagta hai. Colon ka meaning hai: “ab is statement ka block start hone wala hai.” Agar colon miss ho gaya, Python syntax error dega.

```python
if marks >= 40:
    print("Pass")
```

Yahan colon ke baad next line indented hai. Ye indentation Python ko batati hai ki `print("Pass")` if block ke andar hai.

## Indentation ka Role

Indentation Python mein bahut important hai. Indentation ka matlab line ke start mein spaces. Python braces `{}` use nahi karta. Python indentation se samajhta hai ki kaunsi line kis block ke andar hai.

```python
if marks >= 40:
    print("Pass")
print("Program finished")
```

Is example mein `print("Pass")` if block ke andar hai because ye indented hai. `print("Program finished")` if block ke bahar hai because ye left side se start ho raha hai. Ye line condition true ho ya false, dono cases mein run ho sakti hai.

## `=` aur `==` ka Difference

`=` assignment ke liye hota hai. Iska use value store karne ke liye hota hai. `==` comparison ke liye hota hai. Iska use check karne ke liye hota hai ki two values equal hain ya nahi.

```python
marks = 75
print(marks == 75)
```

First line mein `marks = 75` value store kar raha hai. Second line mein `marks == 75` check kar raha hai ki marks 75 ke equal hain ya nahi. Beginners ko ye difference clearly samajhna bahut zaroori hai.

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

# Day 3 - Complete Code Explanation Appendix

Is section mein Day 3 ke basic operator, condition, and loop code examples ko line-by-line simple Hinglish mein explain kiya gaya hai. Aap class mein code dikhane ke baad is section se directly explanation de sakte ho.

## Appendix 1 - Arithmetic Operators Code

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

`a = 10` ek variable create karta hai jiska naam `a` hai. Is variable mein number 10 store hai. Hum is value ko calculations ke liye use karenge.

`b = 3` doosra variable create karta hai. Isme number 3 store hai. Ab `a` and `b` dono numbers hain, so arithmetic operators apply kar sakte hain.

`print("Addition:", a + b)` addition result print karta hai. `"Addition:"` label hai, and `a + b` calculation hai. Python pehle `10 + 3` solve karega, phir output print karega.

`print("Subtraction:", a - b)` subtraction karta hai. `a - b` ka meaning hai 10 minus 3. Output mein label ke saath result show hota hai.

`print("Multiplication:", a * b)` multiplication karta hai. Python mein `*` multiplication symbol hota hai. Yahan 10 multiplied by 3, result 30 hai.

`print("Division:", a / b)` normal division karta hai. `/` operator decimal answer de sakta hai. Isliye output 3.3333 jaisa ho sakta hai.

`print("Remainder:", a % b)` modulus operator use karta hai. `%` division ke baad remainder deta hai. 10 ko 3 se divide karne par remainder 1 hota hai.

`print("Power:", a ** b)` power calculate karta hai. `a ** b` ka matlab 10 power 3, yani 10 * 10 * 10. Output 1000 hota hai.

`print("Floor Division:", a // b)` floor division karta hai. Ye decimal part remove karke integer-style result deta hai. 10 // 3 ka result 3 hota hai.

## Appendix 2 - Relational Operators Code

```python
marks = 75

print(marks > 40)
print(marks == 75)
print(marks != 100)
```

`marks = 75` marks variable mein value 75 store karta hai. Ab hum is value ko compare karenge. Comparison ka result hamesha `True` ya `False` hota hai.

`print(marks > 40)` check karta hai ki marks 40 se greater hain ya nahi. Since 75 greater than 40 hai, result `True` aayega. Ye pass/fail logic mein useful hai.

`print(marks == 75)` equality check karta hai. Dhyan rahe `==` comparison ke liye hota hai, while `=` assignment ke liye hota hai. Yahan marks exactly 75 hain, so output `True`.

`print(marks != 100)` not equal check karta hai. `!=` ka meaning hai equal nahi. Since marks 100 nahi hain, result `True` hoga.

## Appendix 3 - Logical Operators Code

```python
age = 20
has_id = True

print(age >= 18 and has_id == True)
print(age < 18 or has_id == True)
print(not has_id)
```

`age = 20` user ki age store karta hai. Age number hai, so comparison possible hai. Is value ko eligibility check ke liye use karenge.

`has_id = True` boolean value store karta hai. Iska meaning hai user ke paas ID hai. Boolean values condition checks mein useful hoti hain.

`print(age >= 18 and has_id == True)` two conditions combine karta hai. `and` ka rule hai dono conditions true honi chahiye. Age 18 se zyada hai and ID true hai, so final result true.

`print(age < 18 or has_id == True)` `or` operator use karta hai. `or` mein koi ek condition true ho to final result true hota hai. Yahan second condition true hai, so output true hai.

`print(not has_id)` boolean value ko reverse karta hai. Since `has_id` true hai, `not has_id` false ho jayega. `not` ka use reverse logic ke liye hota hai.

## Appendix 4 - Assignment Operators Code

```python
score = 10

score += 5
print(score)

score -= 3
print(score)

score *= 2
print(score)
```

`score = 10` score variable ko initial value deta hai. Starting score 10 hai. Baad mein hum same variable ko update karenge.

`score += 5` ka full meaning hai `score = score + 5`. Old score 10 tha, usme 5 add hua, new score 15 ho gaya. Ye short form code ko clean banata hai.

`print(score)` updated score print karta hai. Is point par output 15 hoga. Print se hum confirm kar sakte hain ki update successful hua.

`score -= 3` ka full meaning hai `score = score - 3`. Current score 15 hai, minus 3 karne par 12 ho gaya. Same variable update hota hai.

`print(score)` current score print karta hai. Output 12 hoga. Ye step-by-step value change observe karne ke liye useful hai.

`score *= 2` ka full meaning hai `score = score * 2`. Current score 12 hai, double hone par 24 ho jata hai. Assignment operators repeated updates ke liye useful hote hain.

`print(score)` final updated score print karta hai. Output 24 aayega. Is example se learners ko variable update ka concept clear hota hai.

## Appendix 5 - Membership Operators Code

```python
students = ["Rahul", "Ayesha", "Priya"]

print("Rahul" in students)
print("Aman" in students)
print("Aman" not in students)
```

`students = ["Rahul", "Ayesha", "Priya"]` ek list create karta hai jisme multiple student names store hain. List square brackets se banti hai. Is list mein hum membership check karenge.

`print("Rahul" in students)` check karta hai ki `"Rahul"` list mein present hai ya nahi. Since Rahul list mein hai, output `True` hoga. `in` operator search jaisa kaam karta hai.

`print("Aman" in students)` check karta hai ki Aman list mein hai ya nahi. Aman list mein nahi hai, so output `False` aayega. Ye attendance/search system ka basic logic hai.

`print("Aman" not in students)` check karta hai ki Aman list mein nahi hai. Since Aman actually list mein nahi hai, result `True` hoga. `not in` negative membership check karta hai.

## Appendix 6 - Identity Operators Code

```python
a = [1, 2, 3]
b = a
c = [1, 2, 3]

print(a is b)
print(a is c)
print(a == c)
```

`a = [1, 2, 3]` ek list create karta hai and usko variable `a` mein store karta hai. Ye list memory mein ek object hoti hai. `a` us object ko refer karta hai.

`b = a` ka matlab hai `b` bhi same list object ko refer karega. Yahan new list create nahi hui. `a` and `b` dono same object ki taraf point kar rahe hain.

`c = [1, 2, 3]` ek new list object create karta hai. Values same hain, but object different hai. Isliye identity check mein difference aayega.

`print(a is b)` check karta hai ki `a` and `b` same object hain ya nahi. Since `b = a` kiya tha, output `True` hoga.

`print(a is c)` check karta hai ki `a` and `c` same object hain ya nahi. Values same hain, but object different hai, so output `False`.

`print(a == c)` values compare karta hai. Since dono lists ke values same hain, output `True` hoga. Isse `is` and `==` ka difference clear hota hai.

## Appendix 7 - Operator Precedence Code

```python
result = 10 + 5 * 2
print(result)

result2 = (10 + 5) * 2
print(result2)
```

`result = 10 + 5 * 2` mein Python multiplication pehle solve karta hai. `5 * 2` pehle 10 hota hai, phir 10 + 10 = 20 hota hai. Ye operator precedence ka example hai.

`print(result)` calculated result print karta hai. Output 20 hoga. Isse students ko samajh aata hai ki Python left-to-right blindly nahi chalta.

`result2 = (10 + 5) * 2` mein brackets priority change kar dete hain. Python pehle bracket solve karega: 10 + 5 = 15. Phir 15 * 2 = 30.

`print(result2)` second calculation ka result print karta hai. Output 30 hota hai. Brackets ka use expression ko clear and controlled banata hai.

## Appendix 8 - if Statement Code

```python
marks = 75

if marks >= 40:
    print("Pass")
```

`marks = 75` marks variable mein number value store karta hai. Ye value condition mein check hogi. Marks ke basis par program decide karega pass print karna hai ya nahi.

`if marks >= 40:` condition line hai. Python check karta hai ki marks 40 ya usse zyada hain. Colon `:` batata hai ki condition ke baad ek block start hone wala hai.

`print("Pass")` if block ke andar hai. Indentation batata hai ki ye line condition ke under belongs karti hai. Condition true hai, so `Pass` print hoga.

## Appendix 9 - if-else Code

```python
marks = 35

if marks >= 40:
    print("Pass")
else:
    print("Fail")
```

`marks = 35` marks variable mein 35 store karta hai. Ye value passing marks se kam hai. Program ab condition ke basis par decision lega.

`if marks >= 40:` check karta hai ki marks 40 ya usse zyada hain ya nahi. Since 35 less than 40 hai, condition false hogi. If block skip ho jayega.

`print("Pass")` sirf tab execute hota jab condition true hoti. Yahan condition false hai, so ye line run nahi hogi.

`else:` alternative block start karta hai. Else ka matlab hai agar if condition false ho, to ye block execute karo. Else ke saath condition nahi likhte.

`print("Fail")` else block ke andar hai. Since marks 35 hain, output `Fail` hoga. Isse decision making ka basic flow clear hota hai.

## Appendix 10 - if-elif-else Grade Code

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

`marks = 82` marks variable mein 82 store karta hai. Python isi value ko multiple conditions ke against check karega. Top to bottom checking hogi.

`if marks >= 90:` first condition hai. Python pehle highest grade check karta hai. 82 >= 90 false hai, so Python next condition par chala jata hai.

`print("Grade A")` sirf tab run hota jab marks 90 ya usse zyada hote. Yahan ye line skip hogi. Indentation batata hai ki ye if block ka part hai.

`elif marks >= 75:` second condition hai. 82 >= 75 true hai, so ye block execute hoga. `elif` multiple conditions ke liye use hota hai.

`print("Grade B")` output print karta hai. Since second condition true hai, Grade B print hoga. Iske baad Python baaki elif/else skip kar deta hai.

`elif marks >= 60:` third condition hai, but yahan tak program nahi aayega because previous condition true ho chuki hai. Ye lower grade range ke liye hoti.

`else:` fallback block hai. Agar koi bhi condition true nahi hoti, tab else run hota. Yahan else run nahi hoga.

## Appendix 11 - Nested Condition Code

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

`age = 20` user ki age store karta hai. Pehli condition age ke basis par check hogi. Agar age 18 se kam hoti, program directly under age bolta.

`has_id = True` boolean variable hai jo batata hai ki user ke paas ID hai. Ye second level condition mein use hoga. Boolean directly condition mein use ho sakta hai.

`if age >= 18:` outer condition hai. Pehle age check hoti hai. Since age 20 hai, condition true hai and program inner condition ke andar jayega.

`if has_id:` inner condition hai. Ye tabhi check hoti hai jab outer condition true ho. Since `has_id` true hai, entry allowed print hoga.

`print("Entry allowed")` inner if block ke andar hai. Age bhi valid hai and ID bhi present hai, so final output entry allowed.

`else: print("ID required")` inner else hai. Agar age valid hoti but ID false hoti, to ID required print hota. Ye nested decision ka second branch hai.

`else: print("Under age")` outer else hai. Agar age 18 se kam hoti, ye block run hota. Isse nested condition ka layered decision flow clear hota hai.

## Appendix 12 - for Loop Code

```python
for number in range(1, 6):
    print(number)
```

`for number in range(1, 6):` loop start karta hai. `range(1, 6)` numbers 1 se 5 tak generate karta hai. Ending value 6 include nahi hoti.

`number` loop variable hai. Har round mein `number` ki value change hoti hai. Pehle 1, phir 2, phir 3, phir 4, phir 5.

`print(number)` loop ke andar hai because indentation hai. Ye line har round execute hoti hai. Isliye output mein 1 se 5 tak numbers print hote hain.

## Appendix 13 - while Loop Code

```python
count = 1

while count <= 5:
    print(count)
    count += 1
```

`count = 1` starting value set karta hai. While loop ko start karne ke liye usually ek control variable chahiye hota hai. Yahan control variable `count` hai.

`while count <= 5:` condition check karta hai. Jab tak count 5 ya usse kam hai, loop repeat hota rahega. Agar condition false ho jaaye, loop stop ho jayega.

`print(count)` current count value print karta hai. Ye line loop ke har round mein execute hoti hai. Output 1, 2, 3, 4, 5 aayega.

`count += 1` count ko har round mein increase karta hai. Ye line bahut important hai. Agar count increase nahi hoga, condition hamesha true rahegi and infinite loop ban sakta hai.

## Appendix 14 - break Code

```python
for number in range(1, 10):
    if number == 5:
        break
    print(number)
```

`for number in range(1, 10):` loop 1 se 9 tak numbers generate karta hai. Har round mein `number` ki value change hoti hai.

`if number == 5:` check karta hai ki current number 5 hai ya nahi. Jab tak number 5 nahi hota, condition false rahegi.

`break` loop ko immediately stop karta hai. Jab number 5 hota hai, break execute hota hai and loop se bahar aa jata hai. Isliye 5 print nahi hota.

`print(number)` break se pehle wale numbers print karta hai. Output 1, 2, 3, 4 hota hai. Break ke baad loop continue nahi hota.

## Appendix 15 - continue Code

```python
for number in range(1, 6):
    if number == 3:
        continue
    print(number)
```

`for number in range(1, 6):` loop 1 se 5 tak chalega. Har round mein number value update hoti hai.

`if number == 3:` check karta hai ki current number 3 hai ya nahi. Jab number 3 hota hai, condition true hoti hai.

`continue` current round ko skip karta hai. Matlab number 3 ke liye neeche ka print execute nahi hoga. Program next loop round par chala jayega.

`print(number)` numbers print karta hai except skipped number. Output 1, 2, 4, 5 hota hai. Continue loop ko stop nahi karta, sirf current iteration skip karta hai.

## Appendix 16 - pass Code

```python
for number in range(1, 4):
    pass
```

`for number in range(1, 4):` loop 1 se 3 tak chalne ke liye ready hota hai. Normally loop ke andar code likhna hota hai.

`pass` ka matlab hai abhi kuch mat karo. Ye placeholder statement hai. Jab future mein code add karna ho but abhi block empty rakhna ho, tab `pass` useful hota hai.

Without `pass`, Python empty block par error dega. Isliye `pass` code structure ko valid rakhta hai. Ye beginner ko samjhana zaroori hai ki `pass` output nahi deta, bas syntax complete karta hai.

---

# Day 3 - Every Code Simple English Explanation

This section explains every important Day 3 code example again in very simple English. Use this section when a learner says, “Sir, code line by line samjha do.” Each line is explained slowly, with the reason behind it.

---

## Code 1 - Arithmetic Operators

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

`a = 10` creates a variable named `a`. This variable stores the number 10. We are keeping this number in a variable so we can reuse it in many calculations. Instead of writing 10 again and again, we can use `a`.

`b = 3` creates another variable named `b`. This variable stores the number 3. Now we have two numeric values: `a` and `b`. These two values will be used to understand different arithmetic operators.

`print("Addition:", a + b)` prints the result of addition. The text `"Addition:"` is only a label for the output. Python first calculates `a + b`, which means `10 + 3`, and then prints the answer.

`print("Subtraction:", a - b)` prints the result of subtraction. Here Python calculates `10 - 3`. The output will show the label and the final answer together.

`print("Multiplication:", a * b)` uses `*` for multiplication. In Python, we do not use `x` for multiplication. Python calculates `10 * 3`, which gives 30.

`print("Division:", a / b)` uses `/` for division. This gives a decimal result because normal division can produce decimal values. Here `10 / 3` gives `3.3333...`.

`print("Remainder:", a % b)` uses `%`, called modulus. It gives the remainder after division. When 10 is divided by 3, remainder is 1, so output is 1.

`print("Power:", a ** b)` uses `**` for power. This means 10 raised to the power 3. In simple words, Python calculates `10 * 10 * 10`.

`print("Floor Division:", a // b)` uses `//` for floor division. It divides the numbers but removes the decimal part. `10 // 3` gives 3.

---

## Code 2 - Relational Operators

```python
marks = 75

print(marks > 40)
print(marks == 75)
print(marks != 100)
```

`marks = 75` creates a variable named `marks`. This variable stores the number 75. We will use this value to compare with other numbers.

`print(marks > 40)` checks if marks are greater than 40. Since 75 is greater than 40, Python returns `True`. Relational operators always return either `True` or `False`.

`print(marks == 75)` checks if marks are exactly equal to 75. Here we use `==` for comparison. Since marks are 75, the result is `True`.

`print(marks != 100)` checks if marks are not equal to 100. Since marks are 75, they are not equal to 100. So Python returns `True`.

---

## Code 3 - Logical Operators

```python
age = 20
has_id = True

print(age >= 18 and has_id == True)
print(age < 18 or has_id == True)
print(not has_id)
```

`age = 20` stores the user's age in a variable. This value will be used to check eligibility. Since age is a number, we can compare it using relational operators.

`has_id = True` stores a boolean value. Boolean means either `True` or `False`. Here `True` means the user has an ID card.

`print(age >= 18 and has_id == True)` uses the `and` operator. `and` means both conditions must be true. Here age is greater than or equal to 18, and `has_id` is also true, so final result is `True`.

`print(age < 18 or has_id == True)` uses the `or` operator. `or` means at least one condition should be true. Here first condition is false, but second condition is true, so final result is `True`.

`print(not has_id)` uses the `not` operator. `not` reverses the boolean value. Since `has_id` is `True`, `not has_id` becomes `False`.

---

## Code 4 - Assignment Operators

```python
score = 10

score += 5
print(score)

score -= 3
print(score)

score *= 2
print(score)
```

`score = 10` creates a variable named `score` and stores 10 in it. This is the starting score. We will update this value step by step.

`score += 5` means add 5 to the current value of score. It is a short form of `score = score + 5`. Old score was 10, so new score becomes 15.

`print(score)` prints the current value of score. At this point, score is 15. This line helps us see the updated value.

`score -= 3` means subtract 3 from the current score. It is a short form of `score = score - 3`. Current score was 15, so new score becomes 12.

`print(score)` prints the updated score again. Now the output will be 12. This confirms that subtraction update worked.

`score *= 2` means multiply current score by 2. It is a short form of `score = score * 2`. Current score was 12, so new score becomes 24.

`print(score)` prints the final value of score. The output will be 24. This shows how one variable can be updated multiple times.

---

## Code 5 - Membership Operators

```python
students = ["Rahul", "Ayesha", "Priya"]

print("Rahul" in students)
print("Aman" in students)
print("Aman" not in students)
```

`students = ["Rahul", "Ayesha", "Priya"]` creates a list of student names. A list can store multiple values in one variable. Here the list contains three names.

`print("Rahul" in students)` checks if `"Rahul"` is present inside the list. Since Rahul is in the list, Python returns `True`.

`print("Aman" in students)` checks if `"Aman"` is present in the list. Aman is not in the list, so Python returns `False`.

`print("Aman" not in students)` checks if Aman is not present in the list. Since Aman is really not present, Python returns `True`.

---

## Code 6 - Identity Operators

```python
a = [1, 2, 3]
b = a
c = [1, 2, 3]

print(a is b)
print(a is c)
print(a == c)
```

`a = [1, 2, 3]` creates a list and stores it in variable `a`. This list is created in memory. Variable `a` points to that list.

`b = a` means variable `b` points to the same list as `a`. No new list is created here. Both `a` and `b` refer to the same object.

`c = [1, 2, 3]` creates a new list. The values are same as list `a`, but memory object is different. So `c` is a separate object.

`print(a is b)` checks if `a` and `b` are the same object. Since `b = a`, both point to the same object, so result is `True`.

`print(a is c)` checks if `a` and `c` are the same object. They have same values but different objects, so result is `False`.

`print(a == c)` checks if values are equal. Since both lists contain `[1, 2, 3]`, result is `True`. This shows the difference between `is` and `==`.

---

## Code 7 - Operator Precedence

```python
result = 10 + 5 * 2
print(result)

result2 = (10 + 5) * 2
print(result2)
```

`result = 10 + 5 * 2` stores the result of an expression. Python solves multiplication first because multiplication has higher priority than addition. So `5 * 2` becomes 10, then `10 + 10` becomes 20.

`print(result)` prints the value stored in `result`. Since the final answer is 20, output will be 20.

`result2 = (10 + 5) * 2` uses brackets. Brackets force Python to solve `10 + 5` first. So bracket result becomes 15, then `15 * 2` becomes 30.

`print(result2)` prints the value of `result2`. Output will be 30. This example shows how brackets can change the result.

---

## Code 8 - Basic if Statement

```python
marks = 75

if marks >= 40:
    print("Pass")
```

`marks = 75` stores marks in a variable. This value will be checked using a condition. The program will decide output based on this value.

`if marks >= 40:` checks whether marks are 40 or more. The colon `:` means the if block is starting. If this condition is true, Python will run the indented line below it.

`print("Pass")` is inside the if block because it is indented. Since marks are 75, the condition is true. So Python prints `Pass`.

---

## Code 9 - if-else Statement

```python
marks = 35

if marks >= 40:
    print("Pass")
else:
    print("Fail")
```

`marks = 35` stores 35 in the marks variable. This value is less than 40, so the pass condition will not be true.

`if marks >= 40:` checks if marks are 40 or more. Since marks are 35, this condition is false. Python will skip the if block.

`print("Pass")` is inside the if block. This line runs only when the condition is true. Here it will not run.

`else:` handles the false case. It does not need any condition. It simply means “if the above condition is false, run this block.”

`print("Fail")` is inside the else block. Since the if condition is false, this line runs and output becomes `Fail`.

---

## Code 10 - if-elif-else Grade System

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

`marks = 82` stores marks in a variable. Python will use this value to decide the grade.

`if marks >= 90:` checks the highest grade condition first. Since 82 is not greater than or equal to 90, this condition is false.

`print("Grade A")` runs only if the first condition is true. Here it is skipped because marks are 82.

`elif marks >= 75:` checks the next condition. Since 82 is greater than or equal to 75, this condition is true.

`print("Grade B")` runs because the previous `elif` condition is true. Python prints Grade B and skips the remaining conditions.

`elif marks >= 60:` is not checked after Grade B is found. In an if-elif-else chain, Python stops after the first true condition.

`else:` is the fallback block. It runs only when none of the above conditions are true. Here it does not run.

---

## Code 11 - Nested Condition

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

`age = 20` stores the age of the user. The outer condition will check this value first.

`has_id = True` stores whether the user has an ID card. This value is used only after age is valid.

`if age >= 18:` checks if the user is adult. Since age is 20, this condition is true, so Python enters this block.

`if has_id:` is the inner condition. It checks if the user has ID. Since `has_id` is True, Python enters this inner block.

`print("Entry allowed")` runs because both conditions are true: age is valid and ID is present.

`else: print("ID required")` belongs to the inner if. It runs only when age is valid but ID is not present.

`else: print("Under age")` belongs to the outer if. It runs only when age is less than 18.

---

## Code 12 - for Loop with range

```python
for number in range(1, 6):
    print(number)
```

`for number in range(1, 6):` starts a loop. `range(1, 6)` gives numbers from 1 to 5. The ending value 6 is not included.

`number` is the loop variable. In every round, it gets a new value. First it becomes 1, then 2, then 3, then 4, then 5.

`print(number)` prints the current value of the loop variable. Since it is inside the loop, it runs again and again until the range is finished.

---

## Code 13 - while Loop

```python
count = 1

while count <= 5:
    print(count)
    count += 1
```

`count = 1` sets the starting value. This variable controls the loop. Without a control variable, while loop logic can become confusing.

`while count <= 5:` checks the condition before every loop round. If count is 5 or less, the loop runs. If count becomes 6, the loop stops.

`print(count)` prints the current value of count. It runs in every loop round because it is indented inside the while block.

`count += 1` increases count by 1 after every round. This line is very important. Without this line, count will stay 1 forever and the loop will never stop.

---

## Code 14 - break

```python
for number in range(1, 10):
    if number == 5:
        break
    print(number)
```

`for number in range(1, 10):` starts a loop from 1 to 9. The loop variable `number` changes in every round.

`if number == 5:` checks if the current number is 5. For numbers 1, 2, 3, and 4, this condition is false.

`break` stops the loop immediately. When number becomes 5, break runs and Python comes out of the loop.

`print(number)` prints the number only if break has not stopped the loop. That is why output prints 1, 2, 3, 4 but not 5.

---

## Code 15 - continue

```python
for number in range(1, 6):
    if number == 3:
        continue
    print(number)
```

`for number in range(1, 6):` starts a loop from 1 to 5. Each number comes one by one.

`if number == 3:` checks if the current number is 3. This condition is true only when loop reaches 3.

`continue` skips the current loop round. When number is 3, Python skips the print line and goes to the next number.

`print(number)` prints all numbers except 3. Output becomes 1, 2, 4, 5. Continue does not stop the loop; it only skips one round.

---

## Code 16 - pass

```python
for number in range(1, 4):
    pass
```

`for number in range(1, 4):` creates a loop from 1 to 3. Python expects some code inside the loop block.

`pass` tells Python to do nothing for now. It is used when we want to keep the block empty temporarily. Without pass, Python will give an indentation or empty block error.

This code does not print anything. It only shows how to keep a block valid when we are not ready to write logic yet.

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

# Day 3 No-Confusion Revision

## Confusion 1 - `if`, `elif`, and `else` kab use karna hai?

Agar sirf one condition check karni hai, to `if` use karo. Agar true and false dono cases handle karne hain, to `if-else` use karo. Agar multiple conditions check karni hain, to `if-elif-else` use karo.

Example: Agar sirf pass check karna hai, `if` enough hai. Agar pass/fail dono print karna hai, `if-else` use karo. Agar grade A/B/C/Fail decide karna hai, `if-elif-else` use karo.

## Confusion 2 - `for` loop aur `while` loop mein difference kya hai?

`for` loop tab use karo jab repeat count clear ho. Example: table 1 se 10 tak print karna. `while` loop tab use karo jab repetition condition par depend kare. Example: jab tak password correct na ho, input mangte raho.

Simple line:

```text
for loop = fixed repetition
while loop = condition-based repetition
```

## Confusion 3 - `range(1, 11)` mein 11 include kyu nahi hota?

Python range ki ending value include nahi karta. `range(1, 11)` ka matlab hai start 1 se karo and 11 se pehle stop ho jao. Isliye output 1 se 10 tak hota hai.

Beginners ko yaad rakhna hai: agar 1 to 10 chahiye, to ending 11 likho. Agar 1 to 5 chahiye, to ending 6 likho.

## Confusion 4 - Indentation error kyu aata hai?

Python indentation se block samajhta hai. Agar `if`, `for`, `while`, `else`, `elif` ke baad line proper spaces ke saath nahi likhi gayi, to indentation error aa sakta hai.

Wrong:

```python
if marks >= 40:
print("Pass")
```

Correct:

```python
if marks >= 40:
    print("Pass")
```

Correct code mein `print("Pass")` line thodi right side shifted hai. Isi shift ko indentation kehte hain.

## Confusion 5 - Infinite loop kya hota hai?

Infinite loop wo loop hota hai jo stop hi nahi hota. Usually while loop mein control variable update nahi karte, tab infinite loop ban sakta hai.

Wrong:

```python
count = 1

while count <= 5:
    print(count)
```

Correct:

```python
count = 1

while count <= 5:
    print(count)
    count += 1
```

Correct code mein `count += 1` hai, isliye count increase hota hai. Jab count 6 hota hai, condition false ho jaati hai and loop stop hota hai.

## Confusion 6 - `break` aur `continue` same hain kya?

Nahi. `break` loop ko completely stop karta hai. `continue` sirf current round skip karta hai. Break ka matlab hai “loop khatam”. Continue ka matlab hai “ye round skip, next round start”.

Example:

```text
break = stop the loop
continue = skip current iteration
```

## Confusion 7 - `%` operator kyu important hai?

`%` remainder deta hai. Even/odd check mein ye very useful hai. Agar number ko 2 se divide karne par remainder 0 hai, to number even hai. Agar remainder 1 hai, to number odd hai.

```python
number = 7
print(number % 2)
```

Output:

```text
1
```

Since remainder 1 hai, number odd hai.

---

# Day 3 Summary

Day 3 mein humne operators, conditions, and loops seekhe. Operators calculation and comparison ke liye use hote hain. Conditions program ko decision making deti hain. Loops repeated work ko easy banate hain.

Important takeaway:

Without conditions, program smart decisions nahi le sakta. Without loops, repeated tasks ke liye same code baar-baar likhna padega. Conditions and loops programming logic ke most important building blocks hain.
