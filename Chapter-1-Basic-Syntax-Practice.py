#     =========================================
#      CHAPTER 1: BASIC SYNTAX & FOUNDATIONS
#     =========================================



# ---- Python Comments (Single & Multi-line) ----

# Single Line Comment..
""" 
    Multiple
  Line Comment.

"""



# ---- Basic Output & Escape Sequences ----

print(35)
print(35 + 66)
print(66 - 35)
print(44 / 2)
print(11 % 5)
print(2 ** 4)
print("My Name Is", "Unknown")
print("My Age Is\n", 18)
print("Ag Og\t", "Bhago G")
print("Hi..", end="!")
print("Bye..")
print("Bye..", "Hi..", sep="!!")
"""
Output =
35
101
31
22.0
1
16
My Name Is Unknown
My Age Is
 18
Ag Og    Bhago G
"""



# ---- Variables & Type Checking (type function) ----

name = "Unknown"
age = 18
cgpa = 9.9
old = False
new = None
print("My Name Is: ", name)
print("My Age Is: ", age)
print("My CGPA Is: ", cgpa)
print(f"My Name {name} Age {age} And CGPA {cgpa}.")

print(type(name))
print(type(age))
print(type(cgpa))
print(type(old))
print(type(new))
"""
Output: 
My Name Is:  Unknown
My Age Is:  18
My CGPA Is:  9.9
My Name Unknown Age 18 And CGPA 9.9 .
<class 'str'>
<class 'int'>
<class 'float'>
<class 'bool'>
<class 'NoneType'>
"""



# ---- String Representations (Single, Double, Triple Quotes) ----

name1 = 'Hey'
name2 = "Hi"
name3 = '''Bye Bye'''
print(name1)
print(name2)
print(name3)
"""
Output:
Hey
Hi
Bye Bye
"""


# ---- Core Python Operators ----

# A. Arithmetic Operators.. { +, -, *, //, /, %, ** }
print("Sum = ", 5 + 2)
print("Difference = ", 5 - 2)
print("Multiply = ", 5 * 2)
print("Divide = ", 5 / 2)
print("Integer Division = ", 5 // 2)
print("Remainder = ", 5 % 2)
print("Power = ", 5 ** 2)
"""
Output:
Sum =  7
Difference =  3
Multiply =  10
Divide =  2.5
Integer Division =  2
Remainder =  1
Power =  25
"""

# B. Relational / Comparison Operators.. { ==, !=, >, <, >=, <= }
a = 4
b = 2
print("Equal To: ", a == b)
print("Not Equal To: ", a != b)
print("Greater Than: ", a > b)
print("Less Than: ", a < b)
print("Greater Than & Equal To: ", a >= b)
print("Less Than & Equal To: ", a <= b)
"""
Output:
Equal To:  False
Not Equal To:  True
Greater Than:  True
Less Than:  False
Greater Than & Equal To:  True
Less Than & Equal To:  False
"""

# C. Assignment Operators.. { =, +=, -=, *=, /=, %=, **=, //= }
i = 22
print(i) # Output = 22

i += 10
print(i) # Output = 32

i -= 10
print(i) # Output = 22

i *= 2
print(i) # Output = 44

i /= 10
print(i) # Output = 4.4

i = 15
i %= 10
print(i) # Output = 5

i **= 2
print(i) # Output = 25

i //= 2
print(i) # Output = 12

# D. Logical Operators.. { not, and, or }
# Note: Precedence Order: { not > and > or }
a = 10
b = 5
print("NOT Operator -> ", not (a < b)) # Output = True
print("AND Operator -> ", (a > b) and (a < b)) # Output = False
print("OR Operator -> ", (a > b) or (a < b)) # Output = True
print(not True and False or True) # Output = True



# ---- String & Numeric Operations ----

# Note: String & Numeric values can operate together using '*'.
A, B = 2, 3
char = "@"
print(A * char * B)
# Output = @@@@@@

# Note: String & String can operate using '*'.
A, B = "2", 3
char = "$"
print((A + char) * B)
# Output = 2$2$2$

# Note: Numeric values can operate with all arithmetic operators.
A, B = 2, 3
C = 4
print(A + B * C)
# Output = 14

# Note: Arithmetic expression with Integer and float will result in float.
A, B = 10, 5.0
C = A * B
print(C)
# Output = 50.0

# Note: Result of division operator with two integers will be float.
A, B = 1, 2
C = A / B
print(C)
# Output = 0.5

# Note: Integer division with float and int will give int displayed as float.
A, B = 1.5, 3
C = A // B
print(C, A / B)
# Output = 0.0 0.5



# ---- Implicit Type Conversion & Advanced Division ----
""" 
Note: floor gives closest integer, which is lesser than or equal to the float value
Result of ( A // B ) is same as floor ( A / B ).
"""
A, B = 12, 5
C = A // B
print(C)
# Output = 2

A, B = -12, 5
C = A // B
print(C)
# Output = -3

A, B = 12, -5
C = A // B
print(C)
# Output = -3

# Note: Remainder is negative when denominator is negative.
A, B = 5, 2
C = A % B
print(C)
# Output = 1

A, B = -5, 2
C = A % B
print(C)
# Output = 1

A, B = 5, -2
C = A % B
print(C)
# Output = -1



# ---- User Inputs & Dynamic Arithmetic ----

num1 = int(input("Enter num1: "))
num2 = int(input("Enter num2: "))

total_sum = num1 + num2
print("Sum = ", total_sum)

diff = num1 - num2
print("Diff = ", diff)

multi = num1 * num2
print("Multiply = ", multi)

div = num1 / num2
print("Divide = ", div)

rem = num1 % num2
print("Remainder = ", rem)

power = num1 ** num2
print("Power = ", power)



# ---- Practical Mini-Programs ----

# Write a Program to input 2 numbers & print their sum.
input1 = int(input("Enter a number: "))
input2 = int(input("Enter a number: "))
print("Sum = ", input1 + input2)
"""
Dry Run:  1. input1 = 2 
          2. input2 = 4
          3. Sum = 2 + 4 = 6
"""

# Write a Program to input side of a square & print its area.
side = int(input("Enter Side of Square: "))
print("The Area Of Square: ", side * side)
"""
Dry Run:  1. Enter Side of Square = 4
          2. The Area Of Square: 4 * 4 = 16
"""

# Write a Program to input 2 floating point numbers & print their average.
n1 = float(input("Enter number: "))
n2 = float(input("Enter number: "))
print("Average: ", (n1 + n2) / 2)
"""
Dry Run:  1. n1 = Enter Number = 4
          2. n2 = Enter Number = 2
          3. Average: (4 + 2) / 2 = (6) / 2 = 3.0
"""
