# write a programme to dispaly some of first n number.
n = int(input("Enter a Number: "))
sum = 0
i = 1
while i<=n:
  sum= sum+i
  i = i+1
print("The sum of first n number: ",n,"is",sum)


# Using Formual without while loop
# sum = n*(n+1)//2
# print("The sum of first n number: ",n,"is",sum)