# Day 3 - Operators, Conditional Statements & Loops

## Topics Covered

Arithmetic Operators, Relational Operators, Logical Operators, Assignment Operators, Membership Operators, Identity Operators, Operator Precedence, Expression Evaluation, if Statement, if-else Statement, if-elif-else, Nested Conditions, Introduction to Loops, for Loop, while Loop, break, continue, pass, Range Function, and Pattern-Based Programs.

Yeh document fresh format mein banaya gaya hai. Har topic individually explain kiya gaya hai. Pehle topic ka meaning hai, phir kyu use karte hain, kya fayda hai, phir practical code, output, aur har code line ka detailed simple Hinglish explanation diya gaya hai.

---

# Day 3 Deep Concept Guide - Har Topic Ko Pehle Detail Mein Samjho

Is section ka goal hai ki learner ko code se pehle concept ka purpose clear ho jaye. Jab tak learner ko yeh nahi samajh aata ki topic kyu use hota hai, tab tak code sirf symbols jaisa lagta hai. Isliye Day 3 mein har topic ko pehle real-life logic se samjho, phir practical code dekho.

## Arithmetic Operators

Arithmetic operators calculation ke tools hain. Jab bhi program mein numbers ke saath maths karni hoti hai, arithmetic operators use hote hain. Addition ke liye `+`, subtraction ke liye `-`, multiplication ke liye `*`, division ke liye `/`, remainder ke liye `%`, power ke liye `**`, and floor division ke liye `//` use hota hai.

Real-life mein billing, marks total, percentage, salary, discount, tax, quantity, and average calculation arithmetic operators se hoti hai. Agar user marks change kare, program automatically total and percentage calculate kar sakta hai. Iska fayda hai ki manual calculation ki zaroorat nahi hoti and result fast milta hai.

## Relational Operators

Relational operators comparison ke liye use hote hain. Ye check karte hain ki value greater hai, smaller hai, equal hai, ya not equal hai. Inka answer hamesha `True` ya `False` hota hai. Example: `marks >= 40` check karega ki marks 40 ya usse zyada hain ya nahi.

Ye operators decision making ka base hain. Pass/fail, eligible/not eligible, correct/wrong password, high/low price jaise decisions relational operators se bante hain. Fayda yeh hai ki program values compare karke smart output de sakta hai.

## Logical Operators

Logical operators multiple conditions ko combine karte hain. `and` tab true hota hai jab dono conditions true ho. `or` tab true hota hai jab koi ek condition true ho. `not` result ko reverse karta hai.

Example: login ke liye username bhi correct hona chahiye and password bhi correct hona chahiye. Movie ticket ke liye age valid ho and ID available ho. Payment ke liye cash or card available ho. Logical operators se real-life complex decision Python mein likhna easy hota hai.

## Assignment Operators

Assignment operators variable mein value store ya update karte hain. `=` value assign karta hai. `+=`, `-=`, `*=`, `/=` old value ko update karte hain. Example: `score += 5` ka matlab hai old score mein 5 add karo and same variable mein store karo.

Loops mein assignment operators bahut useful hote hain. Total calculate karna ho to `total += number` use hota hai. Count increase karna ho to `count += 1` use hota hai. Isse code short and readable hota hai.

## Membership Operators

Membership operators check karte hain ki value kisi collection ke andar present hai ya nahi. Python mein `in` and `not in` use hota hai. Example: `"Rahul" in students` check karega ki Rahul students list mein present hai ya nahi.

Ye attendance, search, cart item check, word search jaise tasks mein useful hai. Fayda yeh hai ki Python direct `True` ya `False` de deta hai, hume manually search logic nahi likhna padta.

## Identity Operators

Identity operators check karte hain ki two variables same memory object ko refer kar rahe hain ya nahi. Python mein `is` and `is not` use hota hai. Ye `==` se different hai. `==` values compare karta hai, `is` identity compare karta hai.

Beginners ke liye simple rule: `==` ka use values compare karne ke liye karo. `is` ka use object identity check ke liye hota hai. Ye advanced concept hai, lekin Day 3 par basic difference clear karna important hai.

## Operator Precedence and Expression Evaluation

Operator precedence batata hai kaunsa operation pehle solve hoga. Maths ki tarah Python mein multiplication addition se pehle hoti hai. Example: `10 + 5 * 2` ka answer 20 hota hai, 30 nahi.

Expression evaluation ka matlab hai Python expression ko step-by-step solve kaise karta hai. Brackets priority change kar dete hain. `(10 + 5) * 2` ka answer 30 hota hai. Fayda yeh hai ki calculation predictable and correct hoti hai.

## if Statement

`if` statement single condition check karta hai. Agar condition true hoti hai, to if block run hota hai. Agar condition false hoti hai, block skip ho jata hai.

Example: agar marks 40 ya zyada hain, to pass print karo. Iska fayda hai ki program condition ke basis par decision le sakta hai.

## if-else Statement

`if-else` true and false dono cases handle karta hai. Agar condition true hai to if block, warna else block. Example: marks 40 ya zyada hain to pass, warna fail.

Fayda yeh hai ki program incomplete nahi rehta. True case ke saath false case bhi handle hota hai. Real programs mein else block user ko clear feedback deta hai.

## if-elif-else

`if-elif-else` multiple conditions ke liye use hota hai. Python top se bottom conditions check karta hai. Jo first condition true hoti hai, uska block run hota hai and baaki skip ho jaati hain.

Grade system, discount slab, age category, salary range, marks range jaise cases mein `if-elif-else` useful hota hai. Isse code structured and readable banta hai.

## Nested Conditions

Nested condition ka matlab condition ke andar condition. Jab decision multiple levels mein ho, tab nested condition use hoti hai. Example: pehle age check karo, phir ID check karo.

Fayda yeh hai ki program layered checking kar sakta hai. Lekin indentation ka dhyan rakhna bahut zaroori hai, kyunki Python indentation se block samajhta hai.

## Introduction to Loops

Loop same code ko baar-baar run karne ke liye use hota hai. Agar hume 1 se 100 tak numbers print karne hain, to 100 print lines likhna bad practice hai. Loop se same kaam few lines mein ho jata hai.

Loops automation ka foundation hain. Counting, tables, patterns, totals, repeated inputs, list processing, sab loops se hota hai.

## for Loop

`for` loop fixed repetition ke liye use hota hai. Jab hume pata ho loop kitni baar chalana hai, tab for loop best hota hai. Example: multiplication table 1 se 10 tak print karna.

For loop `range()` ke saath bahut common hai. `for i in range(1, 11)` ka matlab hai i ko 1 se 10 tak values do and code repeat karo.

## while Loop

`while` loop condition true hone tak repeat hota hai. Jab condition false ho jaati hai, loop stop hota hai. Agar condition kabhi false nahi hoti, infinite loop ban sakta hai.

While loop tab useful hota hai jab repetition count fixed nahi hota. Example: jab tak correct password na mile, input maangte raho.

## break, continue, pass

`break` loop ko completely stop karta hai. `continue` current round skip karta hai. `pass` kuch nahi karta, bas placeholder hota hai.

Example: number 5 aate hi loop stop karna hai to `break`. Number 3 skip karna hai to `continue`. Block empty rakhna hai but syntax valid chahiye to `pass`.

## Range Function

`range()` numbers generate karta hai. Ye mostly for loop ke saath use hota hai. Important rule: ending value include nahi hoti. `range(1, 6)` ka output 1, 2, 3, 4, 5 hota hai.

Range function tables, counting, patterns, repeated tasks, and loop control ke liye bahut useful hai.

## Pattern-Based Programs

Pattern-based programs loops ki practice ke liye use hote hain. Star pattern, number pattern, triangle pattern learners ki logic building improve karte hain.

Patterns se row and repetition ka concept clear hota hai. Beginner ko simple star pattern se start karna chahiye. Isse loop variable ka role deeply samajh aata hai.

---

# 1. Arithmetic Operators

## Topic Samjho

Arithmetic operators calculation ke liye use hote hain. Jaise addition, subtraction, multiplication, division, remainder, power, and floor division. Python mein maths ke liye different symbols use hote hain.

## Kyu Use Karte Hain?

Jab program mein numbers par calculation karni ho, arithmetic operators use karte hain. Billing, marks total, percentage, salary, quantity, discount, tax calculation sab arithmetic operators se hota hai.

## Fayda

Arithmetic operators se program automatically calculation kar sakta hai. User input change kare to output bhi automatically change hota hai.

## Practical Code

```python
a = 10
b = 3

print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)
print("Remainder:", a % b)
```

## Output

```text
Addition: 13
Subtraction: 7
Multiplication: 30
Division: 3.3333333333333335
Remainder: 1
```

## Detailed Code Explanation

| Line | Code | Explanation |
|---|---|---|
| 1 | `a = 10` | `a` variable mein number 10 store kiya gaya hai. Ye first number hai jiske saath calculation hogi. Variable use karne se value reusable ban jaati hai. |
| 2 | `b = 3` | `b` variable mein number 3 store hai. Ye second number hai. Ab `a` and `b` dono numeric variables hain. |
| 4 | `print("Addition:", a + b)` | `a + b` addition karta hai. Python 10 + 3 calculate karta hai. Label ke saath output readable banta hai. |
| 5 | `print("Subtraction:", a - b)` | Ye line 10 - 3 calculate karti hai. Subtraction ka result 7 hota hai. |
| 6 | `print("Multiplication:", a * b)` | Python mein multiplication ke liye `*` use hota hai. Ye line 10 * 3 calculate karke 30 print karti hai. |
| 7 | `print("Division:", a / b)` | `/` normal division karta hai. Division ka result decimal aa sakta hai, isliye output 3.3333 hai. |
| 8 | `print("Remainder:", a % b)` | `%` remainder deta hai. 10 ko 3 se divide karne par remainder 1 hota hai. |

---

# 2. Relational Operators

## Topic Samjho

Relational operators comparison ke liye use hote hain. Ye check karte hain ki value greater hai, smaller hai, equal hai, ya not equal hai. Inka output hamesha `True` ya `False` hota hai.

## Kyu Use Karte Hain?

Decision making ke liye comparison zaroori hota hai. Example: marks 40 se zyada hain ya nahi, age 18 se zyada hai ya nahi, password correct hai ya nahi.

## Fayda

Relational operators se program smart decisions le sakta hai. Ye conditions ka base hain.

## Practical Code

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

## Detailed Code Explanation

| Line | Code | Explanation |
|---|---|---|
| 1 | `marks = 75` | `marks` variable mein 75 store hai. Ye value comparison ke liye use hogi. |
| 3 | `print(marks > 40)` | Ye check karta hai marks 40 se greater hain ya nahi. Since 75 greater hai, output `True` hai. |
| 4 | `print(marks == 75)` | `==` equality check karta hai. Marks exactly 75 hain, so output `True` hai. |
| 5 | `print(marks != 100)` | `!=` not equal check karta hai. Marks 100 nahi hain, so output `True` hai. |

---

# 3. Logical Operators

## Topic Samjho

Logical operators multiple conditions ko combine karte hain. Python mein `and`, `or`, and `not` logical operators hain.

## Kyu Use Karte Hain?

Kabhi-kabhi ek decision ke liye multiple conditions check karni hoti hain. Example: login ke liye username bhi correct hona chahiye and password bhi correct hona chahiye.

## Fayda

Logical operators se complex decision making possible hoti hai. Program ek se zyada conditions ko ek saath evaluate kar sakta hai.

## Practical Code

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

## Detailed Code Explanation

| Line | Code | Explanation |
|---|---|---|
| 1 | `age = 20` | Age variable mein 20 store hai. Ye eligibility check ke liye use hoga. |
| 2 | `has_id = True` | Boolean variable hai jo batata hai ki user ke paas ID hai. |
| 4 | `print(age >= 18 and has_id == True)` | `and` mein dono conditions true honi chahiye. Age valid hai and ID true hai, so output `True`. |
| 5 | `print(age < 18 or has_id == True)` | `or` mein koi ek condition true ho to result true hota hai. Yahan second condition true hai. |
| 6 | `print(not has_id)` | `not` boolean value reverse karta hai. `True` ka reverse `False` hota hai. |

---

# 4. Assignment Operators

## Topic Samjho

Assignment operators variable ki value set ya update karte hain. `=`, `+=`, `-=`, `*=`, `/=` common assignment operators hain.

## Kyu Use Karte Hain?

Jab variable ki old value ko update karna ho, assignment operators useful hote hain. Example: score increase karna, quantity decrease karna, total update karna.

## Fayda

Assignment operators code ko short and clean banate hain. `score += 5` likhna `score = score + 5` ka short form hai.

## Practical Code

```python
score = 10

score += 5
print(score)

score -= 3
print(score)
```

## Output

```text
15
12
```

## Detailed Code Explanation

| Line | Code | Explanation |
|---|---|---|
| 1 | `score = 10` | Score variable ki starting value 10 hai. |
| 3 | `score += 5` | Iska meaning hai score mein 5 add karo. Old score 10 tha, new score 15 ho gaya. |
| 4 | `print(score)` | Updated score print hota hai. Output 15 hai. |
| 6 | `score -= 3` | Current score se 3 subtract hota hai. 15 - 3 = 12. |
| 7 | `print(score)` | Final score print hota hai. Output 12 hai. |

---

# 5. Membership Operators

## Topic Samjho

Membership operators check karte hain ki koi value collection ke andar hai ya nahi. Python mein `in` and `not in` use hote hain.

## Kyu Use Karte Hain?

Search/checking ke liye use hota hai. Example: student list mein naam hai ya nahi, product cart mein item hai ya nahi.

## Fayda

Membership operators se list/string mein value check karna easy hota hai.

## Practical Code

```python
students = ["Rahul", "Ayesha", "Priya"]

print("Rahul" in students)
print("Aman" not in students)
```

## Output

```text
True
True
```

## Detailed Code Explanation

| Line | Code | Explanation |
|---|---|---|
| 1 | `students = ["Rahul", "Ayesha", "Priya"]` | Students naam ki list banayi gayi hai. Is list mein three names stored hain. |
| 3 | `print("Rahul" in students)` | Ye check karta hai Rahul list mein hai ya nahi. Rahul present hai, so output `True`. |
| 4 | `print("Aman" not in students)` | Ye check karta hai Aman list mein nahi hai ya nahi. Aman present nahi hai, so output `True`. |

---

# 6. Identity Operators

## Topic Samjho

Identity operators check karte hain ki two variables same object ko refer kar rahe hain ya nahi. Python mein `is` and `is not` use hote hain.

## Kyu Use Karte Hain?

Ye advanced comparison ke liye use hota hai. Jab hume values nahi, object identity check karni ho tab use karte hain.

## Fayda

Identity operators se samajh aata hai ki two variables memory mein same object point kar rahe hain ya different objects.

## Practical Code

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

## Detailed Code Explanation

| Line | Code | Explanation |
|---|---|---|
| 1 | `a = [1, 2, 3]` | `a` variable ek list object ko refer karta hai. |
| 2 | `b = a` | `b` bhi same object ko refer karta hai jisko `a` refer kar raha hai. |
| 3 | `c = [1, 2, 3]` | `c` ek new list object hai. Values same hain, object different hai. |
| 5 | `print(a is b)` | Same object check hota hai. `a` and `b` same object hain, output `True`. |
| 6 | `print(a is c)` | `a` and `c` different objects hain, output `False`. |
| 7 | `print(a == c)` | `==` values compare karta hai. Values same hain, so output `True`. |

---

# 7. Operator Precedence and Expression Evaluation

## Topic Samjho

Operator precedence batata hai kaunsa operation pehle solve hoga. Expression evaluation ka matlab hai Python expression ko step-by-step solve kaise karta hai.

## Kyu Use Karte Hain?

Correct calculation ke liye precedence samajhna zaroori hai. Agar brackets use nahi kiye to result different aa sakta hai.

## Fayda

Precedence samajhne se calculation errors avoid hote hain.

## Practical Code

```python
result = 10 + 5 * 2
result2 = (10 + 5) * 2

print(result)
print(result2)
```

## Output

```text
20
30
```

## Detailed Code Explanation

| Line | Code | Explanation |
|---|---|---|
| 1 | `result = 10 + 5 * 2` | Python pehle multiplication solve karta hai. `5 * 2 = 10`, phir `10 + 10 = 20`. |
| 2 | `result2 = (10 + 5) * 2` | Brackets ki wajah se addition pehle solve hota hai. `10 + 5 = 15`, phir `15 * 2 = 30`. |
| 4 | `print(result)` | First expression ka answer print hota hai. Output 20 hai. |
| 5 | `print(result2)` | Second expression ka answer print hota hai. Output 30 hai. |

---

# 8. if Statement

## Topic Samjho

`if` statement condition check karta hai. Agar condition true hoti hai, to indented block execute hota hai.

## Kyu Use Karte Hain?

Decision making ke liye `if` use hota hai. Example: marks pass limit se zyada hain to pass print karo.

## Fayda

Program input ke basis par different behavior kar sakta hai.

## Practical Code

```python
marks = 75

if marks >= 40:
    print("Pass")
```

## Output

```text
Pass
```

## Detailed Code Explanation

| Line | Code | Explanation |
|---|---|---|
| 1 | `marks = 75` | Marks variable mein 75 store hai. |
| 3 | `if marks >= 40:` | Condition check hoti hai ki marks 40 ya zyada hain. Colon block start karta hai. |
| 4 | `print("Pass")` | Ye line if block ke andar hai. Condition true hai, so Pass print hota hai. |

---

# 9. if-else Statement

## Topic Samjho

`if-else` two-way decision ke liye use hota hai. Agar condition true hai to if block, warna else block.

## Kyu Use Karte Hain?

Pass/fail, login success/fail, eligible/not eligible jaise decisions ke liye use hota hai.

## Fayda

Program true and false dono cases handle kar sakta hai.

## Practical Code

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

## Detailed Code Explanation

| Line | Code | Explanation |
|---|---|---|
| 1 | `marks = 35` | Marks variable mein 35 store hai. |
| 3 | `if marks >= 40:` | Python check karta hai marks 40 ya zyada hain ya nahi. |
| 4 | `print("Pass")` | Ye line tab run hoti jab condition true hoti. Yahan false hai, so skip hoti hai. |
| 5 | `else:` | Else false case handle karta hai. |
| 6 | `print("Fail")` | Since condition false hai, Fail print hota hai. |

---

# 10. if-elif-else

## Topic Samjho

`if-elif-else` multiple conditions ke liye use hota hai. Python top se bottom conditions check karta hai.

## Kyu Use Karte Hain?

Grade system, category system, price discount, age group jaise multiple decisions ke liye use hota hai.

## Fayda

Multiple possibilities ko clean way mein handle kar sakte hain.

## Practical Code

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

## Detailed Code Explanation

| Line | Code | Explanation |
|---|---|---|
| 1 | `marks = 82` | Marks variable mein value 82 hai. |
| 3 | `if marks >= 90:` | First condition highest grade ke liye check hoti hai. Ye false hai. |
| 4 | `print("Grade A")` | First condition false hone ke karan ye line run nahi hoti. |
| 5 | `elif marks >= 75:` | Second condition check hoti hai. 82 >= 75 true hai. |
| 6 | `print("Grade B")` | True condition mil gayi, so Grade B print hota hai. |
| 7 | `elif marks >= 60:` | Ye condition skip hoti hai kyunki Grade B already decide ho gaya. |
| 9 | `else:` | Else tab run hota jab koi condition true nahi hoti. |

---

# 11. Nested Conditions

## Topic Samjho

Nested condition ka matlab condition ke andar condition. Jab decision multiple levels mein ho, tab nested condition use hoti hai.

## Kyu Use Karte Hain?

Example: Pehle age check karo, phir ID check karo. Dono alag levels ke decisions hain.

## Fayda

Complex decision ko step-by-step handle kar sakte hain.

## Practical Code

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

## Detailed Code Explanation

| Line | Code | Explanation |
|---|---|---|
| 1 | `age = 20` | Age variable mein 20 store hai. |
| 2 | `has_id = True` | Boolean variable batata hai ID available hai. |
| 4 | `if age >= 18:` | Outer condition age check karti hai. |
| 5 | `if has_id:` | Inner condition ID check karti hai. Ye sirf tab check hoti hai jab age valid ho. |
| 6 | `print("Entry allowed")` | Age valid and ID present hai, so entry allowed print hota hai. |
| 7 | `else:` | Inner else ID missing case handle karta hai. |
| 10 | `print("Under age")` | Outer else under age case handle karta hai. |

---

# 12. Introduction to Loops

## Topic Samjho

Loop ka use same code ko baar-baar run karne ke liye hota hai. Repetition ko easy banata hai.

## Kyu Use Karte Hain?

Agar 1 se 100 tak numbers print karne hain, to 100 print lines likhna bad practice hai. Loop se short code mein kaam hota hai.

## Fayda

Loops code ko short, clean, and powerful banate hain.

## Practical Code

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

## Detailed Code Explanation

| Line | Code | Explanation |
|---|---|---|
| 1 | `for number in range(1, 6):` | Loop 1 se 5 tak chalega. `number` har round mein new value leta hai. |
| 2 | `print(number)` | Ye line har round mein current number print karti hai. |

---

# 13. for Loop and Range Function

## Topic Samjho

`for` loop fixed repetition ke liye use hota hai. `range()` numbers generate karta hai. `range(1, 6)` ka output 1 se 5 tak hota hai.

## Kyu Use Karte Hain?

Tables, lists, repeated output, patterns, counting ke liye use hota hai.

## Fayda

For loop predictable repetition ke liye best hai.

## Practical Code

```python
number = 5

for i in range(1, 11):
    print(number, "x", i, "=", number * i)
```

## Output

```text
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

## Detailed Code Explanation

| Line | Code | Explanation |
|---|---|---|
| 1 | `number = 5` | Table ke liye number 5 store kiya gaya hai. |
| 3 | `for i in range(1, 11):` | Loop 1 se 10 tak chalega. Ending 11 include nahi hoti. |
| 4 | `print(number, "x", i, "=", number * i)` | Har round mein table ki ek line print hoti hai. `number * i` multiplication result calculate karta hai. |

---

# 14. while Loop

## Topic Samjho

`while` loop condition true hone tak repeat hota hai.

## Kyu Use Karte Hain?

Jab repetition count fixed nahi hota and condition ke basis par loop chalana ho, tab while loop use hota hai.

## Fayda

While loop dynamic repetition ke liye useful hai.

## Practical Code

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

## Detailed Code Explanation

| Line | Code | Explanation |
|---|---|---|
| 1 | `count = 1` | Count variable starting value set karta hai. |
| 3 | `while count <= 5:` | Jab tak count 5 ya kam hai loop chalega. |
| 4 | `print(count)` | Current count print hota hai. |
| 5 | `count += 1` | Count ko increase karta hai. Ye line loop stop karne ke liye important hai. |

---

# 15. break, continue, pass

## Topic Samjho

`break` loop stop karta hai. `continue` current round skip karta hai. `pass` placeholder hai jo kuch nahi karta.

## Kyu Use Karte Hain?

Loop control ke liye use hote hain. Kab stop karna hai, kab skip karna hai, kab future code ke liye block empty rakhna hai.

## Fayda

Loop behavior ko control kar sakte hain.

## Practical Code

```python
for number in range(1, 6):
    if number == 3:
        continue
    print(number)
```

## Output

```text
1
2
4
5
```

## Detailed Code Explanation

| Line | Code | Explanation |
|---|---|---|
| 1 | `for number in range(1, 6):` | Loop 1 se 5 tak chalega. |
| 2 | `if number == 3:` | Check karta hai current number 3 hai ya nahi. |
| 3 | `continue` | Agar number 3 hai, current round skip hota hai. |
| 4 | `print(number)` | 3 ke alawa baaki numbers print hote hain. |

---

# 16. Pattern-Based Programs

## Topic Samjho

Pattern programs loops ki practice ke liye use hote hain. Ye logic building improve karte hain.

## Kyu Use Karte Hain?

Patterns se nested thinking, repetition, row/column logic, and loop variable ka role clear hota hai.

## Fayda

Pattern practice se problem-solving strong hoti hai.

## Practical Code

```python
rows = 5

for row in range(1, rows + 1):
    print("*" * row)
```

## Output

```text
*
**
***
****
*****
```

## Detailed Code Explanation

| Line | Code | Explanation |
|---|---|---|
| 1 | `rows = 5` | Total rows 5 set ki gayi hain. Pattern 5 lines ka banega. |
| 3 | `for row in range(1, rows + 1):` | Loop 1 se 5 tak chalega. `rows + 1` isliye hai kyunki range ending include nahi karti. |
| 4 | `print("*" * row)` | Star string ko row value ke according repeat karta hai. Row 1 par one star, row 5 par five stars print hote hain. |

---

# Day 3 Final Detailed Code Teaching Notes

## Arithmetic Code Ko Kaise Explain Karna Hai

Jab aap arithmetic code explain karo, students ko bolo ki `a` and `b` two numbers hain. Program in numbers par different mathematical operations perform kar raha hai. `print()` ke andar pehle label hai, phir calculation hai. Label output ko readable banata hai. Calculation Python internally solve karta hai. Isse students ko samajh aata hai ki output mein sirf answer nahi, answer ka meaning bhi show karna important hai.

`a + b` addition hai, `a - b` subtraction hai, `a * b` multiplication hai, `a / b` division hai, and `a % b` remainder hai. Remainder ko specially explain karo because ye learners ke liye new hota hai. Remainder ka practical use even/odd program mein hota hai.

## Relational Code Ko Kaise Explain Karna Hai

Relational code explain karte time students ko bolo ki ye code calculation nahi, comparison kar raha hai. Comparison ka output number nahi hota; output `True` ya `False` hota hai. `marks > 40` ek question jaisa hai: “kya marks 40 se zyada hain?” Python answer deta hai `True`.

`==` ko clearly explain karo. Single `=` value assign karta hai, double `==` value compare karta hai. Beginners aksar yahan mistake karte hain. `!=` ka meaning “not equal” hai. Ye check karta hai ki value same nahi hai.

## Logical Code Ko Kaise Explain Karna Hai

Logical operators explain karte time real-life examples use karo. `and` ka matlab dono conditions true. Example: exam hall entry ke liye admit card bhi chahiye and ID bhi chahiye. `or` ka matlab koi ek condition true. Example: payment cash se ya UPI se ho sakti hai. `not` ka matlab reverse.

Code mein `age >= 18 and has_id == True` dono conditions ko combine karta hai. Agar age valid hai but ID missing hai, final answer false hoga. Isse students ko real decision logic samajh aata hai.

## Condition Code Ko Kaise Explain Karna Hai

Condition code explain karte time pehle `if` ka meaning “agar” batao. `if marks >= 40:` ka meaning hai agar marks 40 ya usse zyada hain. Colon ke baad jo indented block hai, woh condition true hone par run hota hai.

`else` ka meaning “warna” hai. Agar condition false hoti hai, else block run hota hai. `elif` ka meaning “warna agar” hai. Jab multiple conditions hoti hain, Python top se bottom check karta hai and first true block run karta hai.

## Nested Condition Code Ko Kaise Explain Karna Hai

Nested condition mein students ko layered checking samjhao. Pehle outer condition check hoti hai. Agar outer condition true hai, tab inner condition check hoti hai. Example: pehle age valid hai ya nahi, phir ID available hai ya nahi.

Indentation yahan sabse important hai. Inner `if` outer `if` ke andar hota hai, isliye zyada right side indented hota hai. Agar indentation galat hui, Python block galat samjhega ya error dega.

## for Loop Code Ko Kaise Explain Karna Hai

For loop mein `range()` ko slowly explain karo. `range(1, 6)` ka matlab 1 se start karo and 6 se pehle stop ho jao. Isliye output 1 to 5 hota hai. Ending value include nahi hoti.

Loop variable `number` har round mein change hota hai. Pehle 1, phir 2, phir 3, phir 4, phir 5. `print(number)` har round mein run hota hai, isliye multiple outputs aate hain.

## while Loop Code Ko Kaise Explain Karna Hai

While loop mein three parts explain karo: starting value, condition, update. Starting value `count = 1` hai. Condition `count <= 5` hai. Update `count += 1` hai.

Agar update line missing ho, loop infinite ho sakta hai. Isliye while loop mein control variable update karna compulsory habit hai. Students ko dry run karvao: count 1, 2, 3, 4, 5, then 6 par condition false.

## break, continue, pass Ko Kaise Explain Karna Hai

`break` ka meaning hai loop se bahar nikal jao. `continue` ka meaning hai current round skip karo. `pass` ka meaning hai abhi kuch nahi karna.

Break and continue ko compare karke explain karo. Break loop stop karta hai. Continue loop stop nahi karta, sirf ek iteration skip karta hai. Pass output nahi deta, sirf empty block ko valid rakhta hai.

## Pattern Code Ko Kaise Explain Karna Hai

Pattern code mein `rows` total lines decide karta hai. Loop har row ke liye run hota hai. `"*" * row` ka meaning hai star ko row number ke according repeat karo.

Row 1 par one star, row 2 par two stars, row 3 par three stars. Pattern programs se learners ko loop variable ka practical use samajh aata hai. Ye logic building ke liye important hai.
