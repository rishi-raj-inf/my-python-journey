#     =================================================
#        CHAPTER 2: STRING & CONDITIONAL STATEMENTS
#     ================================================


# ---- Strings: Basics & Escape Sequence ----

# Escape Sequence Character {\n, \t}.
str1 = "My Name Is UNKNOWN.\nI'm 18 Years Old."
str2 = "My Name Is UNKNOWN.\tI'm 18 Years Old."
print(str1)
print(str2)
"""
Output = My Name Is UNKNOWN.
         I'm 18 Years Old.
         My Name Is UNKNOWN.     I'm 18 Years Old.
"""

# Concatenation
str3 = "Hello "
str4 = "World"
final_str = str3 + str4
print(final_str)         # Hello World

# Length Of String.
length = len(str3)
print(f"Length: {length}")
# Output = Length: 6

# ---- Strings: Indexing & Slicing ----

# Indexing.
my_str = "UNKNOWN"
print(my_str[0])   # U
print(my_str[1])   # N
print(my_str[2])   # K
print(my_str[3])   # N
print(my_str[4])   # O
print(my_str[5])   # W
print(my_str[6])   # N
# my_str[0] = "#" doesn't support item assignment. You can't change the value using index.

# Slicing. [ starting-idx : ending_idx ] # Ending Index Is Not Included.
# Positive Index.
str5 = "Hello Ji"
print(str5[0:5])           # Hello
print(str5[ :5])           # Hello
print(str5[0: ])           # Hello Ji
print(str5[0:len(str5)])   # Hello Ji

# Negative Index. [ Backward Counting ]
print(str5[-8: ])          # Hello Ji
print(str5[ :len(str5)])   # Hello Ji

# Slicing with Step Argument [ start : ending_idx : step ]
str5 = "Hi Ji"
print(str5[0:5:2])  # Output = H i
# Reverse String Best Trick!
print(str5[::-1])   # Output = iJ iH

# ---- Strings Functions (Modifiers & Finders) ----

str6 = "hey hi vye vye"

# -- Case Modifiers (lower, upper, capitalize, swapcase) --

# str.lower() => Small all char.
print(str6.lower())
# Output = hey hi vye vye

# str.upper() => Capitalizes all char.
print(str6.upper())
# Output = HEY HI VYE VYE

# str.capitalize() => Capitalizes 1st char.
print(str6.capitalize())
# Output = Hey hi vye vye

# The Case Combo: str.swapcase() => Converts all uppercase characters to lowercase and all lowercase characters to uppercase.
# Example: Inverting a badly formatted input.
txt3 = "lOCAL bOY"
swapped = txt3.swapcase()
print(swapped)
# Output = Local Boy

# -- Search & Replace Functions (endswith, startswith, find, rfind, replace, count) --

# str.endswith() => return true if string ends with substring.
print(str6.endswith("ye"))
# Output = True

# str.startswith() => return true if string start with substring.
print(str6.startswith("hey"))
# Output = True

# str.find() => return 1st index of 1st occurrence.
print(str6.find("hi"))
# Output = 4

# The Reverse Finder.
""" str.rfind(sub) => Searches the string from the right side and 
                      returns the highest index where the substring is found.
                      Returns -1 if not found.
"""
# Example: Extracting file name from a full path.
file_path = "C:/Users/Admin/Downloads/malware.exe"

# Aakhri '/' kahan par hai uska index nikalna.
last_slash_index = file_path.rfind("/")
print(last_slash_index)
# Output = 24

# Slicing ka use karke sirf file ka naam nikalna.
file_name = file_path[last_slash_index + 1 : ]
print(file_name)
# Output = malware.exe

# str.replace(old, new) => replaces all occurrences of old.
print(str6.replace("vye", "Bye"))
# Output = hey hi Bye Bye

# str.count("abc") => counts the occurrence of substring.
print(str6.count("vye"))
# Output = 2

# -- Stripping & Padding (strip, lstrip, rstrip, zfill) --

# str.strip("  abc  ") => Removing Extra Space.
str6 = "  hey hi Bye Bye  "
print(str6.strip())
# Output = hey hi Bye Bye

# str.lstrip([chars]) => Removes leading (left-side) characters from the string. (Default is space)
# str.rstrip([chars]) => Removes trailing (right-side) characters from the string. (Default is space)
str66 = "  Hi  "
print(f"lstrip: '{str66.lstrip()}'") # Output = lstrip: 'Hi  '
print(f"rstrip: '{str66.rstrip()}'") # Output = rstrip: '  Hi'

str66 = "00_Hi_11"
print(f"lstrip: '{str66.lstrip('0')}'") # Output = lstrip: '_Hi_11'
print(f"rstrip: '{str66.rstrip('1')}'") # Output = rstrip: '00_Hi_'

# The Binary/Padding Combo.

# str.zfill() => Pads the string on the LEFT with zeros ('0') until it reaches the specified total length (width).
# Example 1: Standard number formatting.
binary_data = "101"
padded_data = binary_data.zfill(8)
print(padded_data)
# Output = 00000101 (Total Length 8 Ho Gayi Hai)

# Example 2: Handling Negative Numbers. (The Smart Logic)
negative_val = "-22"
padded_neg = negative_val.zfill(5)
print(padded_neg)
# Output = -0022  (Minus Sign Ke Baad Zero Fit Kiya Hai)

"""
Note: Real World Use Case.
1. Networking & Binary Alignment: Computer networking ya binary cryptography mein data ko hamesha
                                  fix bits (jaise 8-bit, 16-bit, ya 32-bit) mein align karna hota hai.
                                  Agar tumhara binary code chota hai, toh zfill() se use easily standard
                                  size ka banaya jata hai.
2. Database Padding/Roll Numbers: Universities mein IDs ya Roll Number ka format fix hota hai (jaise 0001,
                                  0015, 0102). Jab user input deta hai, toh woh sirf 1, 15, ya 102 likhta hai.
                                  zfill() ka use karkey database mein use proper formal structure mein badal diya jata hai.
3. Time & Date Formatting: Agar koi time 9:5 likhta hai, toh use standardized format 09:05 mein badalne ke liye minutes aur
                           hours par zfill(2) lagaya jata hai.
"""

# -- Splitting & Joining (split, rsplit, splitlines, join) --

# str.split() => Data Extraction.
str6 = "username@pagal.com"
splt = str6.split("@")
print("First Index:", splt[0])  # Output = First Index: username
print("Second Index:", splt[1]) # Output = Second Index: pagal.com
print("Split List: ", splt)     # Output = Split List:  ['username', 'pagal.com']

""" Note: Normal split() string ko aage (left) se todta hai.
          rsplit(separator, maxsplit) string ko piche (right) se todta hai.
          Agar hum maxsplit (limit) define nahi karengey, toh split aur rsplit
          ka output bilkul same aayega. Iska asli use tab hai jab humey aakhri ke 1-2 words
          ko alag karna ho bina poori string ko tode.
""" 
print(f"split(): {str6.split('@')}, rsplit(): {str6.rsplit('@')} & Output: Same")
# Output = split(): ['username', 'pagal.com'], rsplit(): ['username', 'pagal.com'] & Output: Same

# Example: Extracting the file extension from a complex file name.
file_name = "report.2026.final.pdf"

# Normal str.split() => Left se todta hai.
left_split = file_name.split(".", 1)
print(left_split)
# Output = ['report', '2026.final.pdf']

# The Reverse Splitter.
# str.rsplit() => Right se todta hai.
right_split = file_name.rsplit(".", 1)
print(right_split)
# Output = ['report.2026.final', 'pdf']

# The Multi-Line Master.
# str.splitlines() => Splits a multi-line string at line breaks (\n) and returns a list containing each line as an element.

# Example: Breaking a multi-line server log into an analyzable list.
server_log = """Error 404: Page Not Found
Warning : CPU overload at 90%
Access Granted: Bruce Wayne Logged in"""

# Har ek line ko ek list item bana do.
log_list = server_log.splitlines()

# Pura list print karte hain.
print(log_list)
# Output = ['Error 404: Page Not Found', 'Warning: CPU overload at 90%', 'Access Granted: Bruce Wayne Logged in']

# Ab hum loop laga kar kisi bhi specific line ko check kar sakte hai.
print(f"First event: {log_list[0]}")
# Output = First event: Error 404: Page Not Found

# str.join(iterable) => Joins the elements of a list (or iterable) into a single string, using the string as a separator (glue).
web_Folder = ["https:", "users", "admin", "name", "admitcard", "download", ".com"]
site_path = "//".join(web_Folder)
print(site_path)
# Output = https://users//admin//name//admitcard//download//.com


# ---- String Functions (The is_ Checkers) ----

# -- Core Boolean Checkers (isdigit, isalpha, isalnum, islower, isupper, isspace) --

# str.isdigit() => The Number Checker.
# Example: Verifying a Security Pin.
pin1 = "4048"
pin2 = "40 48" # Space is present
pin3 = "4048A" # Alphabet is present
print(pin1.isdigit()) # Output = True
print(pin2.isdigit()) # Output = False
print(pin3.isdigit()) # Output = False

# str.isalpha() => The Alphabet Checker.
# Example: Validating a First Name.
name_1 = "Python"
name_2 = "Python3"      # Number is present
name_3 = "Mr Python"    # Space is  present
print(name_1.isalpha()) # Output = True
print(name_2.isalpha()) # Output = False
print(name_3.isalpha()) # Output = False

# str.isalnum() => The Alphanumeric Checker.
# Example: Validating a Username format.
user1 = "Admin01"
user2 = "Admin@01" # Special Character makes it False
print(user1.isalnum()) # Output = True
print(user2.isalnum()) # Output = False

# str.islower() => The Lowercase Checker.
# Example: Checking strict lowercase constraints.
text1 = "admin321" # Numbers are ignored, checks only letters
text2 = "Admin123"
print(text1.islower()) # Output = True
print(text2.islower()) # Output = False

# str.isupper() => The Uppercase Checker.
# Example: Validating a PAN Card format.
pan1 = "ABCDE1234F"
pan2 = "Abcde1234F"
print(pan1.isupper()) # Output = True
print(pan2.isupper()) # Output = False

# str.isspace() => The Blank Space Checker
# Example: Blocking empty form submissions.
input1 = "  "
input2 = " Admin "
print(input1.isspace()) # Output = True (Block this!)
print(input2.isspace()) # Output = False

# -- Advanced & Legacy Checkers (istitle, isprintable, isascii, isidentifier, isnumeric) --

# The Title Checker.
# str.istitle() => Returns True if the first letter of EVERY word in the string is uppercase, and the rest are lowercase.
# Example: Checking formal name formatting.
nam1 = "Anant True"
nam2 = "Anant true"
print(nam1.istitle()) # Output = True
print(nam2.istitle()) # Output = False

# The Visibility Checker.
# str.isprintable() => Returns True if all characters are visible/printable on screen (No hidden escape character like \n or \t).
# Example: Blocking payloads with hidden line-breaks.
safe_text = "Hello World"
hacked_text = "Hello\nWorld"
print(safe_text.isprintable())   # Output = True
print(hacked_text.isprintable()) # Output = False

# The ASCII Checker.
# str.isascii() => Returns True if the string contains ONLY standard English keyboard characters (ASCII), otherwise False.
# Example: Blocking non-English /suspicious characters.
txt1 = "Admin"
txt2 = "Adminहम" # Contains Hindi Characters
print(txt1.isascii()) # Output = True
print(txt2.isascii()) # Output = False

# The Variable Name Checker.
# str.isidentifier() => Returns True if the string is a valid Python variable name (No spaces, cannot start with a number).
# Example: Checking valid variable naming rule.
var1 = "total_sum"
var2 = "1st_sum"   # Cannot start with a number
var3 = "total sum" # Cannot have space
print(var1.isidentifier()) # Output = True
print(var2.isidentifier()) # Output = False
print(var3.isidentifier()) # Output = False

# The Numeric/Math Checker.
# str.isnumeric() => Returns True if all characters are numeric, including advanced mathematical characters like fractions (1/2).
# Example: Differentiating between standard digits and numeric symbols.
tet1 = "123"
tet2 = "½"
# isdigit() fraction ko False bolta hai, par isnumeric() True bolta hai.
print(tet1.isdigit()) # Output = True
print(tet1.isnumeric()) # Output = True
# But..
print(tet2.isdigit()) # Output = False
print(tet2.isnumeric()) # Output = True


# ---- Conditional Statements (if-Elif-Else) ----

age = int(input("Enter Your Age: "))
if age >= 18:
    print("Vote")
else:
    print("Can't Vote")
# Output = Vote [input -> age = 19]


light = input("Enter Light Colour : ").lower()
if light == "red":
    print("Stop..!!")
elif light == "yellow":
    print("Look..")
elif light == "green":
    print("Go..")
else:
    print("Light is broken..")
# Output = Stop..!! [input -> light = red]


marks = int(input("Enter Your Marks : "))
if marks >= 90 and marks <= 100:
    print("A++")
elif marks >= 80 and marks < 90:
    print("A+")
elif marks >= 70 and marks < 80:
    print("A")
elif marks >= 60 and marks < 70:
    print("B")
elif marks >= 50 and marks < 60:
    print("C")
elif marks >= 33 and marks < 50:
    print("D")
else:
    print("Fail..")
# Output = A++ [input -> marks = 98]

food = input("Enter Food : ").upper()
eat = "Yes" if food == "CAKE" else "No"
print(eat)
# Output = Yes [input -> Food = cake]

print("Yes") if food == "CAKE" or food == "JALEBI" else print("No")
# Output = No [input -> food = halwa]

vote = int(input("Enter Your Age : "))
vote = ("No", "Yes")[vote >= 18]
print(vote)
# Output = No [input -> age = 17]

# ---- Nested Conditional Statements (If inside If) ----

# Example: Cybersecurity Login and Authorization Check.
username = input("Enter Username: ").lower().strip()
password = input("Enter Password: ")

if username == "admin":
    if password == "01-inf":
        print("Access Granted! Welcome Admin.")
    else:
        print("Access Denied: Wrong Password.")
else:
    print("Access Denied: Invalid Username.")
"""
Dry Run:
Step1: If -> Username = True & Password = True
Step2: Checking Outer Condition -> Username == True
Step3: Checking Inner Condition -> Password == True
Step4: Output = Access Granted! Welcome Admin.
But..
Step1: If -> Username = True & Password = False
Step2: Checking Outer Condition -> Username == True
Step3: Checking Inner Condition -> Password == False
Step4: Output = Access Denied: Wrong Password.
But..
Step1: If -> Username = False
Step2: Output = Access Denied: Invalid Username.
"""

# ---- Practical Mini-Programs ----

# Write a program to input user's first name & print its length.
str7 = input("Enter Your Name : ")
len1 = len(str7)
print(f"Length Of Your Name : {len1}")
"""
Dry Run:- 1. Enter Your Name : UNKNOWN
          2. len = 7
          3. Length Of Your Name :7
"""

# Write a program to find occurrence of '$' in a string.
str8 = "$ Dollar Hui $ Hui Hui $"
count = str8.count("$")
print(f"The Occurrence Of '$' : {count}")
# Output = The Occurrence Of '$' : 3

# Write a program to check if a number entered by the user is odd or even.
num3 = int(input("Enter A Number : "))
if num3 % 2 == 0:
    print("Even")
else:
    print("Odd")

# Write a program to find the greatest of 3 numbers entered by the user.
a = int(input("a : "))
b = int(input("b : "))
c = int(input("c : "))
if a >= b and a >= c:
    print(f"The Largest Number Is : {a}")
elif b >= c:
    print(f"The Largest Number Is : {b}")
else:
    print(f"The Largest Number Is : {c}")

# Write a program to find the greatest of 4 numbers entered by the user.
a1 = int(input("a = "))
b1 = int(input("b = "))
c1 = int(input("c = "))
d1 = int(input("d = "))
if a1 >= b1 and a1 >= c1 and a1 >= d1:
    print(f"The Largest Number Is : {a1}")
elif b1 >= c1 and b1 >= d1:
    print(f"The Largest Number Is : {b1}")
elif c1 >= d1:
    print(f"The Largest Number Is : {c1}")
else:
    print(f"The Largest Number Is : {d1}")

# Write A Program To Check If A Number Is A Multiple Of 7 Or Not.
num4 = int(input("Enter A Number : "))
if num4 % 7 == 0:
    print(f"{num4} Is A Multiple Of 7")
else:
    print(f"{num4} Is Not A Multiple Of 7")
