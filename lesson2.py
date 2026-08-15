name = "Dhanya"
age = 18
cgpa = 8.6
print(type(cgpa))
print(type(age))
print(type(name))

#keywords in python
#for, if else, while, break, continue, def, return, import, from, as, pass, class, try, except, finally, with, lambda, yield, global, nonlocal, assert, del

#print sum of two numbers
num1 = int(input("Enter first number:"))
num2 = int(input("Enter second number:"))
sum = num1 + num2
print("Sum of two numbers is:", sum)





#type conversion
#1.Implicit type conversion(automatic)
#python automatically converts smaller data types to larger ones to prevent data loss
#for eg: x = 3, y= 3.5, z = x + y, here x is int and y is float, so python converts x to float and then adds them

#2.Explicit type conversion(manual)
#manually converts data types using built-in functions like int(), float(), str(), etc.
#for eg: x = "10", y = int(x), print(y+5), output:15


x = 3
y = 4.5
z = x+y
print("Value of z:", z)
print("Data type of z is:", type(z))

#take num as input from user and convert it to float and print both original and converted value
num = input("Enter a number:")
convertedValue = float(num)

print("Original value is:", num, "and its data type is:", type(num))

print("Converted value is:", convertedValue, "and its data type is:", type(convertedValue))



