operation = input("Please enter an operation (addition, subtraction, multiplication, division). ")
num1 = int(input("Please enter a number. "))
num2 = int(input("Please enter another number. "))

if operation == "addition":
  print(num1 + num2)
elif operation == "subtraction":
  print(num1 - num2)
elif operation == "multiplication":
  print(num1 * num2)
elif operation == "division":
  print(num1 / num2)
else:
  print(f"'{operation}' is not a valid operation, please try again.")
