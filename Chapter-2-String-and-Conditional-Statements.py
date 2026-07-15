#     =================================================
#        CHAPTER 2: STRING & CONDITIONAL STATEMENTS
#     ================================================


# ---- 50 Questions & Their Codes ----


# ---- BLOCK 1: String Basics, Indexing & Slicing ----

# Q.1. String ke aakhri 3 characters nikaalein.
n1 = "Balance"
last_3_char = n1[-3:]
print(last_3_char)
"""
Dry Run: B  a  l  a  n  c  e
        -7 -6 -5 -4 -3 -2 -1
        last_3_char = n1[-3:len(n1)]
        Output = nce
"""

# Q.2. String ko reverse karke print karein.    [ Using Slice and "".join( reversed(str) ) ]

# First Method.
n4 = "ELPPA"
rev = n4[::-1]
print(rev)
# Output = APPLE

# Second Method.
rev2 = "".join(reversed(n4))
print(rev2)
# Output = APPLE

# Q.3. String ke beech ka character nikaalein.
n7 = "Programming"
str_mid = n7[len(n7) // 2]
print(str_mid)
# Output = a

# Q.4. String "Python" ko 3 baar print karein. [ String Multiplication ]
n9 = "Python"
print(n9 * 3)
# Output = PythonPythonPython

# Q.5. String indexing "Cyber" ke pehle 2 aur aakhri ke 2 characters ko jod kar ek naya word banayein.
n33 = "Cyber"
print(n33[:2] + n33[-2:])
"""
Dry Run: n33 = Cyber
         n33[:2] = "Cy", n33[-2:] = "er"
         "Cy" + "er" = "Cyer"
         Output = Cyer
"""


# ---- BLOCK 2: Case Modifiers &  Cleaners ----

# Q.6. String mein saare spaces ko underscore(_) se badlein.
n3 = "Python Is A High Level Programming Language."
replace_space = n3.replace(" ", "_")
print(replace_space)
# Output = Python_Is_A_High_Level_Programming_Language.

# Q.7. Ek string "Hello World" ko "hello world" mein badlein. [ Using .lower() function ]
n6 = "Hello World"
chg_lower = n6.lower()
print(chg_lower)
# Output = hello world

# Q.8. Swapcase: Capital ko small aur small ko capital karein. [ Using .swapcase() function ]
n32 = "lOCAL bOY"
print(n32.swapcase())
# Output = Local Boy

# Q.9. Pad a short network binary fragment to standard 8-bit length. [ Using .zfill() function ]
binary_frag = "1011"
padded_frag = binary_frag.zfill(8)
print(f"8-bit Data: {padded_frag}")
# Output = 8-bit Data: 00001011

# Q.10. Remove unwanted leading and trailing space from a noisy login input. [ Using .strip() function ]
noisy_input = "  admin_root  "
clean_input = noisy_input.strip()
print(f"Cleaned Input: '{clean_input}'")
# Output = Cleaned Input: 'admin_root'


# ---- BLOCK 3: Search , Extract & Advanced Parsers ----

# Q.11. Check Karein Ki Kya String "Python" Se Shuru Hoti Hai ? [ Using .startswith() function. ]
n2 = "Python Expert"
is_start = n2.startswith("Python")
print(is_start)
# Output = True

# Q.12. Kisi string mein 'z'ka index (position) dhundein. [ Using .find() function ]
n8 = "ABzCD"
find_z = n8.find("z")
print(find_z)
# Output = 2

# Q.13. Check karein kya file executable (.exe) hai? [ Using .endswith() function ]
file_name = "malware_payload.exe"
print("Executable File!" if file_name.endswith(".exe") else "Normal File")
# Output = Executable File!

# Q.14. Extract the domain name from a target email address. [ Using .split() function ]
target_email = "admin@secure-server.com"
domain = target_email.split("@")[1]      # It's same as -> domain = target_email.split("@") then, print(domain[1])
print(f"Target Domain: {domain}")
"""
Dry Run: target_email.split("@") -> ['admin', 'secure-server.com']
         Index [1] -> secure-server.com
         Output = Target Domain: secure-server.com
"""

# Q.15. Count frequency of 'o' in "WoooWoo". [ Using .count() function ]
n31 = "WooWoo"
print(n31.count("o"))
# Output = 4

# Q.16. String Find vs Index: Check karein kya string mein '@' hai, agar nahi toh error na aaye.
# => Logic :- .find() use karney par -1 deta hai agar nahi mila to aur wahi  .index() error deta hai.
n35 = "unknown@gmail.com"
print("Not Found" if n35.find('@') == -1 else f"Found at index {n35.find('@')}")
# Output = Found at index 7

# Q.17. Word Counter (Basic): Ek sentence mein kitne words hai?
n36 = "Hi Hello Bye Bye"
print(n36.count(" ") + 1) # + 1 for last word because, .count() function only count spaces for word.
# Output = 4

# Q.18. Extract only the malicious executable name from a full system path. [ Using .rfind() function ]
file_path = "C:/Users/Admin/Downloads/malware.exe"
last_slash_index = file_path.rfind("/")
file_name = file_path[last_slash_index + 1 :]
print(f"Extracted File: {file_name}")
"""
Dry Run: file_path.rfind("/") -> 24
         file_path[last_slash_index + 1 :] -> malware.exe
         Output = Extracted File: malware.exe
"""

# Q.19. Split a multi-line server log into an analyzable list and extract the first event. [ Using .splitlines() function ]
server_log = """Access Denied
CPU 99%
System Halted"""
event_list = server_log.splitlines()
print(f"Critical Event: {event_list[0]}")
# Output = Critical Event: Access Denied

# Q.20. Ek list of words ko join karke ek proper URL/Path banayein. [ Using .join() function ]
folders = ["https:", "", "api.server.com", "v1", "auth"]
full_url = "/".join(folders)
print(f"Generated URL: {full_url}")
# Output = Generated URL: https://api.server.com/v1/auth


# ---- BLOCK 4: String Checkers & Validators ----

# Q.21. Check karein ki string "123" poori numeric hai ya nahi. [ Using .isdigit() function ]
n5 = "1234"
is_numeric = n5.isnumeric()
print(is_numeric)
# Output = True

# Q.22. Check karein kya string khali(empty) toh nhi hai?
n10 = ""
print(len(n10) == 0)
# Output = True

# Q.23. Vowel or Consonant Check. [ Using 'in' ]
n20 = "i"
print("Vowel" if n20 in "aeiou" else "Consonant")
# Output = Vowel

# Q.24. Form submission security: Check karein kya user ne sirf blank space toh nahi bheja. [ Using .isspace() function ]
user_input = "   "
print("Blocked: Empty Input" if user_input.isspace() else "Accepted")
# Output = Blocked: Empty Input

# Q.25. Check karein kya saare characters alphabets hai( no numbers ).
n25 = "123abc456def"
print("Yes" if n25.isalpha() else "No")
# Output = No

# Q.26. String Palindrome: Kya "madam" ulta karne par wahi rehti hai?
n26 = "Madam"
print("Palindrome" if n26.lower() == n26[::-1].lower() else "Is Not Palindrome")
# Output = Palindrome

# Q.27. Check if string is Upper Case. [ Using .isupper() function ]
n28 = "UPPER"
print("Yes" if n28.isupper() else "No")
# Output = Yes

# Q.28. Check if a payload contains hidden escape characters (\n, \t). [ Using .isprintable() function ]
payload = "root_login\naccess_granted"
print("Safe" if payload.isprintable() else "Warning: Hidden character detected!")
# Output = Warning: Hidden character detected!

# Q.29. Username Validation: Check karein kya username mein sirf alphabets aur numbers hain (No special characters). [ Using .isalnum() function ]
new_user = "Admin@123"
print("Valid Username" if new_user.isalnum() else "Invalid: Special characters not allowed.")
# Output = Invalid: Special characters not allowed.

# Q.30. Verify if a newly created system variable name is strictly valid. [ Using .isidentifier() function ]
var_name = "1st_payload"
print("Valid" if var_name.isidentifier() else "Invalid Variable Name")
# Output = Invalid Variable Name


# ---- BLOCK 5: Built-in Math Utilities ----

# Q.31. Convert "10" (string) to int and check if it's > 5.
n30 = "10"
print(f"{n30} is greater than 5" if int(n30) > 5 else f"{n30} is less than 5")
# Output = 10 is greater than 5

# Q.32. Absolute difference: Hamesha positive result nikalein (a-b). [ Using abs(a-b) function ]
f = 4
g = 6
print(abs(f - g))
# Output = 2 [Without abs function Output is '-2']

# Q.33. Convert total bruteforce timeout seconds into Minutes and Seconds. [ Using divmod() ]
total_timeout = 222
mins, secs = divmod(total_timeout, 60)
print(f"Timeout: {mins} Minutes and {secs} Seconds")
# Output = Timeout: 3 Minutes and 42 Seconds

# Q.34. Multiple threat severity scores mein se sabse highest score nikaalein. [ Using max() function ]
print(f"Max Threat Level: {max(25, 89, 45, 99, 12)}")
# Output = Max Threat Level: 99
print(f"Min Threat Level: {min(25, 89, 45, 99, 12)}")
# Output = Min Threat Level: 99


# ---- BLOCK 6: Conditional Logic (Core Decisions) ----

# Q.35. Check karein number Even hai ya Odd.
n11 = int(input("Enter Number: "))
if n11 % 2 == 0:
    print(f"'{n11}' Is A Even Number.")
elif n11 % 2 != 0:
    print(f"'{n11}' Is A Odd Number.")
else:
    print("Enter Valid Number")
"""
Dry Run: Enter Number: 22
         22 % 2 == 0 [ True ]
         Output = '22' Is A Even Number.
"""

# Q.36. Age check karke batayein: 18+ (Adult), 13-17 (Teen), <13 (Child).
n12 = int(input("Enter Your Age: "))
if n12 > 18 and n12 < 60:
    print("Adult")
elif n12 >= 13 and n12 <= 18:
    print("Teen")
elif n12 > 0 and n12 < 13:
    print("Child")
elif n12 >= 60:
    print("Old")
else:
    print("Invalid Number.")
"""
Dry Run: Enter Your Age: 19
         19 > 18 and 19 < 60 [ True ]
         Output = Adult
"""

# Q.37. Do numbers mein se bada(Greater) kaunsa hai?
n13 = int(input("a = "))
n14 = int(input("b = "))
print(f"'{n13}' is a greatest number." if n13 > n14 else f"'{n14}' is a greatest number.")
"""
Dry Run: a = 22 & b = 2
         22 > 2 
        '22' is a greatest number.
"""

# Q.38. Check karein kya given number 3 aur 5 dono se divide hota hai?
n15 = int(input("Enter Number: "))
print("Yes" if n15 % 3 == 0 and n15 % 5 == 0 else "No")
"""
Dry Run: Enter Number: 15
         15 % 3 == 0 and 15 % 5 == 0
         True and True = True
         Output = Yes
"""

# Q.39. Positive, Negative ya Zero.
n17 = int(input("Enter Number: "))
if n17 > 0:
    print(f"{n17} is a Positive Number.")
elif n17 < 0:
    print(f"{n17} is a Negative Number.")
elif n17 == 0:
    print(f"{n17} is Zero.")
else:
    print("Invalid Number")
"""
Dry Run: Enter Number: 12
         12 > 0 [ True ]
         Output = 12 is a Positive Number.
"""

# Q.40. Leap Year Check (Standard Logic).
n18 = int(input("Enter Year: "))
print("Leap" if (n18 % 4 == 0 and n18 % 100 != 0) or (n18 % 400 == 0) else "No")
"""
Dry Run: Enter Year: 2024
         (2024 % 4 == 0 and 2024 % 100 != 0) or (2024 % 400 == 0)
         ( True and True ) or ( False ) = True or False = True
         Output = Leap
"""

# Q.41. Grade System: 90+(A), 80+(B), 70+(C).
n19 = int(input("Enter Your Marks: "))
if n19 >= 90 and n19 <= 100:
    print("Grade: A")
elif n19 >= 80 and n19 < 90:
    print("Grade: B")
elif n19 >= 70 and n19 < 80:
    print("Grade: C")
elif n19 >= 33 and n19 < 70:
    print("Grade: D")
elif n19 >= 0 and n19 < 33:
    print("Fail")
else:
    print("Invalid Number.")
"""
Dry Run: Enter Your Marks: 89
         1. 89 >= 90 and 89 <= 100
            False and True = False
         2. 89 >= 80 and 89 < 90
            True and True = True
            Output = Grade: B
"""

# Q.42. Check karein kya given number 10 se 50 ke beech mein hai?
n22 = 22
print(10 <= n22 <= 50)
# Output = True

# Q.43. Triangle validity: Kya teeno side ka sum 180 hai?
t = 55
r = 80
i = 45
print("Is a triangle" if (t + r + i) == 180 else "Is not a triangle")
# Output = Is a triangle


# ---- BLOCK 7: Practical Mini-Programs & Nested Logic ----

# Q.44. User se password mangiye, agar "admin" hai toh "Welcome".
n16 = input("Enter Password: ")
print("Welcome" if n16 == "admin" else "Wrong Password.")
"""
Dry Run: Enter Password: owner
         owner == admin [ False ]
         Output = Wrong Password.
"""

# Q.45. Teen numbers mein se sabse bada ( Greatest Of 3 ).
a = 2
b = 22
c = 222
if a >= b and a >= c:
    print(f"{a} is a greatest number.")
elif b >= a and b >= c:
    print(f"{b} is a greatest number.")
else:
    print(f"{c} is a greatest number.")
"""
Dry Run: 1. 2 >= 22 and 2 >= 222
            False and False = False
         2. 22 >= 2 and 22 >= 222
            True and False = False
         3. Output = 222 is a greatest number.
"""

# Q.46. Login Logic: Username aur Pin dono check karein.
ipt_name = input("Username: ")
ipt_pin = input("Pin: ")

user_name = "Admin"
pin = "tata@89"

# First Method
print("Welcome." if user_name == ipt_name and pin == ipt_pin else "Wrong.")
"""
Dry Run: Username: "Admin" and Pin: "tata@89"
         user_name == "Admin" and pin == "tata@89"
         True and True = True
         Output = Welcome.
"""

# Second Method.
if user_name == ipt_name:
    if pin == ipt_pin:
        print("Access Granted! Welcome Admin.")
    else:
        print("Access Denied: Wrong Password.")
else:
    print("Access Denied: Invalid Username.")
"""
Dry Run: Username: "Admin" and Pin: "tata@89"
         Step 1. user_name == "Admin" [True]
         Step 2. pin == "tata@89" [True]
         Step 3. Output = Access Granted! Welcome Admin.
"""

# Q.47. Nested if: Agar number positive hai, toh check karein wo even hai ya odd.
n23 = int(input("Enter Number: "))
if n23 > 0:
    if n23 % 2 == 0:
        print(f"{n23} is Positive Even Number.")
    else:
        print(f"{n23} is Positive Odd Number.")
"""
Dry Run: Enter Number: 12
         Step1: 12 > 0 [ True ]
         Step2: 12 % 2 == 0 [ True ]
         Output = 12 is Positive Even Number.
"""

# Q.48. Calculator: User input operator(+,-) ke hisab se calculate karein.
x = int(input("x = "))
y = int(input("y = "))
o = input("Enter Operator(+,-): ")
print(f"{x} + {y} = {x+y}" if o == "+" else f"{x} - {y} = {x-y}" if o == "-" else "Invalid Operator")

# Q.49. Username Length: Check karein username 5-15 characters ka hai.
n27 = "Bullet"
print(f"Welcome {n27}" if len(n27) >= 5 and len(n27) <= 15 else "Username range (5-15)")
# Output = Welcome Bullet

# Q.50. Multi-level Discount: Price > 1000(20%), >500(10%).
p_price = 2200
dis = 0.2 if p_price > 1000 else 0.1 if p_price > 500 else 0
print(p_price - (p_price * dis))
"""
Dry Run: p_price = 2200
         Step1: 2200 > 1000 [ True ], dis = 0.2
         Step2: 2200 - (2200 * 0.2) = 2200 - 440 = 1760
         Output = 1760.0
"""