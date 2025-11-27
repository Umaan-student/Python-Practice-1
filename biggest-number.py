# Give 3 Number and find which Number is biggest

num1 = int(input("Enter a first Number: "))
num2 = int(input("Enter a Secound Number: "))
num3 = int(input("Enter a Third Number: "))

print("1st number =", num1, "2nd number =", num2, "3rd number =", num3)

if num1 > num2 and num1 > num3:
    print("first Number is biggest =", num1)
elif num2 > num1 and num2 > num3:
    print("secound Number is biggest =", num2)
elif num3 > num2 and num3 > num1:
    print("Third Number is biggest =", num3)
else:
    print("all number are equal")
