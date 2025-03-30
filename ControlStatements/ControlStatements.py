#============= ====================if else Statement ===========================================
# Case1
a=30
if a>20:
    print("true condition")
else:
    print("false condition")

# Case2
if True:
    print("true condition")
else:
    print("false condition")

# Case3
if 1:
    print("true condition")
else:
    print("false condition")

# Even or Odd
a=10
if a%2==0:
    print("Even Number")
else:
    print("Odd Nmber")
	
# Multiple statements under if block
if False:
    print("Statement1")
    print("Statement2")
    print("Statement3")
else:
    print("Statement4")
    print("Statement5")

print("Statement6") # Separate statement , Not part of else Block
# Single Line

print("welcome") if True else print("Python")
print("welcome") if False else print("Python")

print("welcome") if 20>10 else print("Python")
print("welcome") if 20<10 else print("Python")

a=10
print("Even num") if a%2==0 else print("Odd number")


# Multiple statements with condition in Single Line
{print("Python2"),print("learning1")} if True else {print("Python3"), print("learning4")}
{print("Python2"),print("learning1")} if False else {print("Python6"), print("learning7")}

# ===================================elif ===========================================

# elif
a=50
if a==10:
    print("Ten")
elif a==20:
    print("Twenty")
elif a==30:
    print("Thirty")
else:    # Optional
    print("Not listed")

# ===================================Range() function ===========================================

#Range() function
print(list(range(10))) #[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(list(range(5,10))) #[5, 6, 7, 8, 9]
print(list(range(1,10,2))) #[1, 3, 5, 7, 9] Odd numbers
print(list(range(0,10,2))) #[0, 2, 4, 6, 8] Even numbers
print(list(range(10,1,-1))) #[10, 9, 8, 7, 6, 5, 4, 3, 2] Decrement
print(list(range(-10,-5))) #[-10, -9, -8, -7, -6]   Nagitives
print(list(range(-10,-5,2))) #[-10, -8, -6] Nagitives increment by 2
print(list(range(-1,-11,-1))) # it will increment and print form -1 to -10
print(list(range(10))[3:8])  # [3, 4, 5, 6, 7] slicing 3 - 8 , but it will ignore last element
print(list(range(10))[5]) # [5] accesses the element at index 5 in the list.
print(range(5).start, range(5).stop) # .start returns the starting value of the range, which is 0.
# .stop returns the stopping value of the range, which is 5 (though 5 is not included in the generated sequence).


# ===================================for loop ===========================================
#for loop

#Prints 1..9 numbers
for i in range(10):
    print(i)

#Prints Evens between 2..9 numbers
for i in range(2,10,2):
    print(i)

#Prints Odds between 1..9 numbers
for i in range(1,10,2):
    print(i)

#Prints numbers between 10..2 in decending order
for i in range(10,1,-1):
    print(i)

# ===================================while loop ===========================================
#Prints 1..9 numbers
i=1
while i<=10:
    print(i)
    i=i+1

#Prints 10..1 numbers in decending order
i=10
while i>=1:
    print(i)
    i=i-1

# ===================================break & Continue ===========================================
#break
for i in range(1,10):
    if i==5:
        break
    print(i)
print("program exited")


#continue
for i in range(1,10):
    if i==5:
        continue
    print(i)
print("program exited")










