# Give 3 Number and find which Number is biggest
num1 = int(input("Enter a first Number: "))
num2 = int(input("Enter a secound Number: "))
num3 = int(input("Enter a Third Number: "))

if num1>num2 and num1>num3:
  print("first number is biggest")
elif num2>num1 and num2>num3:
  print("secound number is biggest")
elif num3>num1 and num3>num2:
  print("Third number is biggest")
else:
  print("All number are Same")
