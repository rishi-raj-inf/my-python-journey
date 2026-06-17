print("Hello World")

#     =========================================
#         CHAPTER 1: VARIABLES & DATA TYPES
#     =========================================


# ---- 40 Questions & Their Codes ----

# Q.1. Apna Name aur College ka naam variables mein store karke print karein.
name = "Python"
cllg = "Programming"
print("Hi, My name is", name, "& My college is", cllg)
# Output = Hi, My name is Python & My college is Programming

# Q.2. Do numbers ka multiply karein.
num1 = 5
num2 = 45
print("5 * 45 =", num1 * num2)
# Output = 5 * 45 = 225

# Q.3. Square of a number.
num3 = 17
print("Square Of 17 = ", num3 * num3)
# Output = Square Of 17 =  289

# Q.4. Float value print karein.
pi = 3.14
print("The Value Of Pi is", pi)
# Output = The Value Of Pi is 3.14

# Q.5. Simple Greeting.
name1 = "C"
print(name1 + " Programming.")
# Output = C Programming.

# Q.6. Modulo Operator (%) se remainder nikalein.
num4 = 5
num5 = 17
print("17 % 5 =", num5 % num4)
# Output = 17 % 5 = 2
# Note: Agar left value choti ho (5 % 17), toh remainder hamesha left value (5) hi aayega..

# Q.7. Power Operator(**).
num6 = 2
power = 4
print("2^4 =", num6 ** power)
# Output = 2^4 = 16

# Q.8. Floor Division (//).
num7 = 2
num8 = 5
print("Floor Division: 5 // 2 = ", num8 // num7)
print("Division: 5 / 2 = ", num8 / num7)
""" 
    Output = Floor Division: 5 // 2 =  2 [Lesser Value]
             Division: 5 / 2 =  2.5
"""

# Q.9. String ko integer main badlein. [Type Casting]
strr = int("22")
print(type(strr))
# Output = <class 'int'>
# Note: strr = int("wh") or int("2.5") then, Output = invalid literal for int() with base 10: 'wh' or '2.5' [Error]..

# Q.10. Calculate Cube of a number.
num9 = 9
power = 3
print("9^3 =", num9 ** power)
# Output = 9^3 = 729

# Q.11. Simple Interest Calculator.
p = 1220
r = 22
t = 5
si = (p * r * t) / 100
print("Simple Interest =", si)
# Output = Simple Interest = 1342.0

# Q.12. Area of Circle.
r = 4
aracr = 3.14 * r * r
print("Area of circle :", aracr)
# Output = Area of circle : 50.24

# Q.13. Temperature Converter (Celsius to Fahrenheit).
cel = 37
fah = (cel * (9/5)) + 32
print("Fahrenheit =", fah)
# Output = Fahrenheit = 98.60000000000001

# Q.14. Average of 3 marks.
n1 = 20
n2 = 10
n3 = 30
avg = (n1 + n2 + n3) / 3
print("Average :", avg)
# Output = Average : 20.0

# Q.15. Use of len() function.
var = "whatever"
vari = "0123"
print(len(var), ",", len(vari))
# Output = 8 , 4

# Q.16. Swapping without 3rd variable (Python Way).
a = 55
b = 65
a, b = b, a
print("a =", a, "& b =", b)
# Output = a = 65 & b = 55

# Q.17. Swapping With Arithmetic.
a = 10
b = 5
a = a + b
b = a - b
a = a - b
print("a =", a, "& b =", b)
# Output = a = 5 & b = 10
"""
Dry Run:   a = 10
           b = 5
           a = a + b = 10 + 5 = 15
           b = a - b = 15 - 5 = 10
           a = a - b = 15 - 10 = 5
           a = 5 & b = 10
"""

# Q.18. Check if Character is in String. (Using 'in' Operator)
strr = "Whatever"
char = "ever"
print(char in strr)
# Output = True

# Q.19. Find ASCII value of a character. (Using 'ord()' function)
print(ord("A"))
# Output = 65

# Q.20. Get Character from ASCII. (Using 'chr()' function)
print(chr(65))
# Output = A

# Q.21. XOR (^) Operator For Encryption.
data = 6
key = 4
encrypted = data ^ key
lock_open = encrypted ^ key 
print(lock_open)  # ( A ^ Key ) ^ Key = A
"""
Dry Run:   XOR(^) = Same Bits -> {0,0} and {1,1} output -> {0}, Different Bits -> {1,0} and {0,1} output -> {1}
           (data = 6 = 0110), (key = 4 = 0100), (encrypted = 2 = 0010)
           encrypted = data ^ key = 0110 ^ 0100 = 0010 (2)
           lock_open = encrypted ^ key = 0010 ^ 0100 = 0110 (6)
"""

# Q.22. Bitwise Left Shift (Scaling).
#  [ Scaling: X << Y = X * 2^Y ]  Ex: 5 << 2 = 5 * 2^2 = 20
x = 2
print(2 << 3)
"""
Dry Run:   2 (0010)
           0010 First Left Shift = 00100
           00100 Second Left Shift = 001000
           001000 Third Left Shift = 0010000
           0010000 (16)
           Formula: 2 << 3 =  2 * 2^3 = 2 * 8 = 16
"""

# Q.23. Bitwise Right Shifting (Scaling).
# [ Scaling Right: X >> Y = X / 2^Y ] Ex: 4 >> 2 = 4 / 2^2 = 4 / 4 = 1
x = 8
print(x >> 2)
"""
Dry Run:   8 (1000)
           1000 First Right Shift 0100
           0100 Second Right Shift 0010
           0010 (2)
           Formula -> 8 >> 2 = 8 / 2^2 = 8 / 4 = 2
"""

# Q.24. Identity Operator (is). ( Using for Memory Optimization in Large Models )
x = None
print(x is None)
# Output = True
# But..
list1 = [1, 2, 3]
list2 = [1, 2, 3]
print(list1 == list2) # Data Same Output Is True
print(list1 is list2) # Memory Number Not Same Output Is False
# Output = True, False

# Q.25. Complex Math for AI.
"""
Format: a + bj
a = Real Number (Asli hissa)
b = Imaginary Number (Kaalpnik hissa, jiske aage j laga ho.)
Note: In Electronics & Engineering 'i' is reserve for Electric Current that's why we use in Python 'j' or 'J' for Imaginary Number.
"""
x = 4 + 6j
y = complex(2, 3)

print("First Real Number :", x.real)
print("Second Real Number :", y.real)
print("First Imaginary Number :", x.imag)
print("Second Imaginary Number :", y.imag)

print("Add Two Complex Numbers :", x + y)
print("Subtract Two Complex Numbers :", x - y)
"""
Output = First Real Number : 4.0
         Second Real Number : 2.0
         First Imaginary Number : 6.0
         Second Imaginary Number : 3.0
         Add Two Complex Numbers : (6+9j)
         Subtract Two Complex Numbers : (2+3j)
"""

# Q.26. Boolean Logic Inversion.
ok = False
print(not ok)
# Output = True

# Q.27. User Profile Creator. ( Using f"" String )
name = input("Enter Your Name : ")
age = int(input("Enter Your Age : "))
city = input("Enter Your City Name : ")
print(f"Hi.. My Name is {name}, I'm {age} years old & I'm from {city}.")
# Output = Hi.. My Name is Umbrella, I'm 2 years old & I'm from Rain.

# Q.28. Body Mass Index (BMI) Calculator. [ Formula :- Weight / ( Height^2 ) ]
weight = int(input("Enter Your Weight(kg) : "))
height = float(input("Enter Your Height(m) : "))
b_m_i = (weight / (height ** 2))
print(f"Your Body Mass Index Is {round(b_m_i, 2)}.")
# Output = Your Body Mass Index Is 17.36.

# Q.29. Simple Bill Calculator.
p_pri = float(input("Enter Product Price : "))
p_quan = int(input("Enter Product Quantity : "))
p_total = p_pri * p_quan
p_gst = p_total * 0.18
p_final = p_total + p_gst
print(f"The Product Total Price With 18% GST Is {round(p_final, 2)}.")
# Output = The Product Total Price With 18% GST Is 302.7.

# Q.30. Days To -> Years, Month, Weeks & Days.
days = int(input("Enter Days : "))
years = days // 365
remain_day_y = days % 365
month = remain_day_y // 30
remain_day_m = remain_day_y % 30
weeks = remain_day_m // 7
extra_days = remain_day_m % 7
print(f"{years} Years, {month} Months, {weeks} Weeks & {extra_days} Days.")
"""
Dry Run:  1. Enter Days = 500
          2. Years = 500 // 365 = 1
            .Remaining Days After Year = 500 % 365 = 135
          3. Months = 135 // 30 = 4
            .Remaining Days After Month = 135 % 30 = 15
          4. Weeks = 15 // 7 = 2
          5. Days = 15 % 7 = 1
            Result: 1 Years, 4 Months, 2 Weeks & 1 Days.
"""

# Q.31. Minutes to Hours and Minutes.
to_min = int(input("Enter Minutes : "))
hrs = to_min // 60
min = to_min % 60
print(f"{hrs} Hours & {min} Minutes.")
"""
Dry Run:   to_min = 256
           hrs = 256 // 60 = 4
           min = 256 % 60 = 16
           Result = 4 Hours & 16 Minutes
"""

# Q.32. Remainder and Quotient Together.
x = int(input("Enter Number : "))
div = int(input("Enter Divider : "))
print(f"{x % div} Remainder & {x // div} Quotient.")
# Output = 2 Remainder & 29 Quotient. [x = 89 & div = 3]

# Q.33. Data Masking (String Repetition for Dummy Data).
# Password length ke hisaab se '*' generate karna..
pwd_ln = 8
masked_pwd = "*" * pwd_ln
print(f"Secured Password Field: {masked_pwd}")
# Output = Secured Password Field: ********

# Q.34. Memory Address Extraction (id function).
# Ek secret payload ka RAM address (Memory location) nikalna..
payload = "XYZ_Attack_String"
memo_loca = id(payload)
print(f"Payload stored at memory address: {memo_loca}")
# Output = Payload stored at memory address: 191246000****

# Q.35. Multiline String (Configuration Setup).
# AI Server ka configuration ek multiline string mein store karein..
server_config = """
Server: AI-Node-INF
Status: Active
Port: 0101
Firewall: Enabled
Data: Secure
Encrypted: True
"""
print(server_config)
"""
Output = 
Server: AI-Node-INF
Status: Active
Port: 0101
Firewall: Enabled
Data: Secure
Encrypted: True
"""

# Q.36. Round-Robin Server Routing (Modulo Operator).
# 5 servers hain (0, 1, 2, 3, 4). Agar 127th packet aaye, toh wo kis server par jayega..
total_server = 5
packet_number = 127
assigned_server = packet_number % total_server
print(f"Packet {packet_number} routed to Server Index: {assigned_server}")
# Output = Packet 127 routed to Server Index: 2

# Q.37. Confidence Score Percentage (Float Math).
# AI model ka confidence score 0.7484 hai. Ise clean percentage mein badlein..
raw_score = 0.7484
prcntg_score = int(raw_score * 100)
print(f"AI Threat Detection Confidence: {prcntg_score}%")
# Output = AI Threat Detection Confidence: 74%

# Q.38. Boolean Logic: Threat Level Check.
threat_score = int(input("Enter threat score (1-100): "))
is_critical = threat_score > 75
print(f"Critical Threat Detected: {is_critical}")
# Output = Critical Threat Detected: False [input = 72]

# Q.39. Bandwidth Consumption (Typecasting & Math).
# Ek user ne 9.5 GB data use kiya. Ise exact integer MB me convert karein. (1 GB = 1024 MB)..
user_GB = float(input("Enter Data Used in GB: "))
used_MB = int(user_GB * 1024)
print(f"Total Bandwidth Consumed: {used_MB} MB")
# Output = Total Bandwidth Consumed: 9728 MB

# Q.40. Finding Variable Data Type Dynamically.
incoming_Data = "404_Error"
data_Type = type(incoming_Data)
print(f"The data type of incoming payload is: {data_Type}")
# Output = The data type of incoming payload is: <class 'str'>
