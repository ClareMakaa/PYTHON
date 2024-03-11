#Type conversion is converting data from one type to another
#1. Converting int data to str.
num1 = 5
num2 = 8
print("This output")

#(A))Python Implicit Type Conversion - automatic type conversion
#Example where Python promotes the conversion of the lower data type (integer) to the higher data type (float) to avoid data loss.
integer_number = 123
float_number = 1.23
new_number = integer_number + float_number
print("Value:",new_number)
print("Data Type:",type(new_number)) #we can see new_number has value 124.23 and is of the float data type.


#(B))Explicit Type Conversion/Typecasting - manual type conversion
num_string = "12"
num_integer = 23
print("Data type of num_string before Typecasting:", type(num_string))

num_string = int(num_string)
print("Data type of num_string after Typecasting:", type(num_string))

num_sum = num_integer + num_string
print("Sum:" ,num_sum)
print("Data type of num_sum:", type(num_sum))