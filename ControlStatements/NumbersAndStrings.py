# ======= Python Numbers ======================================

# Number Types & conversions

# Example1:
x = 10  # int
y = "welcome"  # string
z = True  # boolean
w = 10.5  # float

print(type(x))
print(type(y))
print(type(z))
print(type(w))

# Example2:
x = 10  # int
y = "welcome"  # string
z = True  # boolean
w = 10.5  # float

print(type(float(x)))  # valid   int --> float
print(type(int(w)))  # valid  float --> int

print(type(int(z)))  # valid  boolean --> int
print(type(float(z)))  # valid  boolean --> float

# print(type(int(y)))  # invalid
# print(type(float(y)))  # invalid

# ======= max() and min()functions on Numbers =========
print("max of 80, 100, 1000:", max(80, 100, 1000))
print("max of -10, 10, 5:", max(-10, 10, 5))

print("min of 80, 100, 1000:", min(80, 100, 1000))
print("min of -10, 10, 5:", min(-10, 10, 5))

# =====================Pythin Strings=================================

# Creating strings
name = "John"  # a string
mychar = 'S'  # a character
print(name)
print(mychar)

# you can also use the following syntax to create strings.
name1 = str()  # this will create empty string object
name2 = str("newstring")  # string object containing 'newstring'
print("This will create a empty string : ",name1)
print(name2)

single_quote = 'RockyBhai, Yash'; print(single_quote)
double_quote = "RockyBhai, Yash"; print(double_quote)


multi_line = '''This is a
multi-line string'''
print(multi_line)

first_name = "Rocky"
last_name = "bhai"
full_name = first_name + " " + last_name
print(full_name)  # Output: John Doe

repeated_string = "Ha" * 3
print(repeated_string)  # Output: HaHaHa

greeting = "Hello"
print(greeting[0])  # Output: H



# ========Strings are immutable=========================
str1 = "RockyBhaiYash"
str2 = "RockyBhaiYash"

print(id(str1), id(str2))  # 2563776772912 ,2563776772912

str2 = str2 + "to python"
print(id(str1), id(str2))  # 2563776772912 ,2563776821744(changed means immutable)

# ==========  + and * with string========================
Str = "RockyBhaiYash"
print(Str + " to Python programming")  # welcome to Python programming
print(Str * 3)  # welcomewelcomewelcome

# ============Slicing==============
Str = "ROCKINGSTARYASH"
print(Str[1:3])  # OC
print(Str[:7])  # ROCKING
print(Str[4:])  # INGSTARYASH
print(Str[1:-1])  # OCKINGSTARYA # elimate 1 char from end
print(Str[1:-2])  # OCKINGSTARYA  #eleminate 2 chars from end

# ============ord() and chr() Functions==============
"""ord() and chr() Functions in Python
#--------------------------------------------------------------------------
The ord() and chr() functions are used to convert between characters 
and their corresponding ASCII (or Unicode) values.
#--------------------------------------------------------------------------
ord() Function: 
This function takes a single character (a string of length 1) as an argument
 and returns an integer representing its Unicode (ASCII) code point.
#--------------------------------------------------------------------------
chr() Function: This function takes an integer representing a Unicode code point 
and returns the corresponding character"""
print(ord('A'))  # 65
print(chr(65))  # A

# =============String Functions in Python==========
print(len("hello"))  # 5
print(max("abc"))  # c
print(min("abc"))  # a

# ===================in  and not in  operators=====
s1 = "Welcome"
print("come" in s1)  # True
print("come" not in s1)  # False

# ==============Strings comparison================
print("tim" == "tie")  # False
print("free" != "freedom")  #True
print("arrow" > "aron")  #True
print("right" >= "left")  #True
print("teeth" < "tee")  #False
print("yellow" <= "fellow")  #False
print("abc" > "")  #True

# =============Iterating string using for loop==================
s = "hello"
for i in s:
    print(i)
    # print(s, end="\n")  #this is default behavior
    # print(s, end="")    # print string without a newline
    # print(s, end="foo")  # now print() will print foo after every string

quote = "Yash said, \"Hello!\""
print(quote)  # Output: She said, "Hello!"
# Special characters can be included in strings using a backslash (\):

# Newline: \n
# Tab: \t
#Backslash: \\
# Quotes: \' or \"
# --------------------------------------------
s = "Python"
i = 0

while i < len(s):
    print(s[i])
    i += 1


# ===============Testing strings====================
s = "welcome to python"
print(s.isalnum())  #False
print("Welcome".isalpha())  #True
print("2012".isdigit())  #True
print("first Number".isidentifier())  #False
print(s.islower())  #True
print("WELCOME".isupper())  #True
print(" ".isspace())  #True


# ===========Searching for Substrings==================

s = "welcome to python"
print(s.endswith("thon"))  # True
print(s.startswith("good"))  # False
print(s.find("come"))  #3
print(s.find("become"))  #-1
print(s.count("o"))  #3

# ===============Converting Strings================
s = "String in PYTHON"
s1 = s.capitalize()
print(s1)  #String in python

s2 = s.title()
print(s2)  #String In Python

s3 = s.lower()
print(s3)  #string in python

s4 = s.upper()
print(s4)  #STRING IN PYTHON

s5 = s.swapcase()
print(s5)  #sTRING IN python

s6 = s.replace("in", "on")
print(s6)  #String on PYTHON

print(s)  #String in PYTHON
