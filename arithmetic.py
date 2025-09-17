num1=int(input("Enter the first integer:"))
num2=int(input("Enter the second integer:"))
addition=num1+num2
subtraction=num1-num2
multiplication=num1*num2
if num2 != 0:
    division = num1 / num2
else:
    division = "Not defined"
print("Addition:",addition)
print("Subtraction:",subtraction)
print("Multiplication:",multiplication)
print("Division:",division)

