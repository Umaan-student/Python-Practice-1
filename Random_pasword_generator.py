import random
chars = "abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*ABCDEFGHIJKLMNOPQRSTUVWXYZ10"
length=int(input("enter your length: "))
pasword=""
for a in range(length):
  pasword+=random.choice(chars)
print(pasword)