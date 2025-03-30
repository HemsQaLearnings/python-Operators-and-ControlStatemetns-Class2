# implicit method
# Example 1
# lower data type to higher data type to avoid data loss
# integer to float
int_num = 124
flo_num =1.23
new_num = int_num+flo_num

print("datatype of int_num : ",type(int_num))
print("datatype of flo_num : ",type(flo_num))
print("value of new_num : ",new_num)
print("value of new_num : ",type(new_num))

# ------------Example 2: inter to String ( lower to higher )-------------------------------
# integer to String
int_num = 124
str_num = "478"
print("datatype of int_num : ",type(int_num))
print("datatype of flo_num : ",type(str_num))
# print(int_num+str_num)

# it cannot be performed such type of operations using the implicit conversion method. Neverthless,
# we can use the explicit conversion method to perform these types of opeartions.

# ----------------Example 3 : Explicit Type Conversion ------------------------


int_num1 = 100
str_num2 = "478"

print("Data type of int_num1:", type(int_num1))
print("The data type of str_num before Explicit Type Conversion:", type(str_num2))

# Explicit type conversion from str to int
# Syntax: <required_datatype>(expression)
str_num1 = int(str_num2)
print("Data type of str_num after Explicit Type Conversion:", type(str_num1))

# Summing the two integers
sum_of_num2 = int_num1 + str_num1

print("Sum of int_num and str_num:", sum_of_num2)
print("The data type of the sum of numbers:", type(sum_of_num2))

