# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.# ==========================================
# 🐍 PYTHON PRACTICE PROGRAMS – ID, TYPE, BIN, OCT, HEX, INT
# ==========================================

# ---------- PART 1: id() and type() Function ----------

# 1. Find ID of a variable
a = 10
print("1. ID of a =", id(a))

# 2. Check data type of variable
x = 25
print("2. Type of x =", type(x))

# 3. Same value → same ID (small integers are cached)
a = 100
b = 100
print("3. ID of a and b:", id(a), id(b))

# 4. Different objects with same value (strings)
s1 = "hello"
s2 = "hello"
print("4. ID of s1:", id(s1))
print("   ID of s2:", id(s2))

# 5. Different data types
a = 10
b = 10.5
c = "10"
print("5. Type of a, b, c:", type(a), type(b), type(c))

# 6. Type of boolean variable
flag = True
print("6. Type of flag =", type(flag))

# 7. Type of list variable
numbers = [1, 2, 3]
print("7. Type of numbers =", type(numbers))

# 8. Type of tuple variable
data = (10, 20, 30)
print("8. Type of data =", type(data))

# 9. Type of dictionary variable
person = {"name": "Aisha", "age": 20}
print("9. Type of person =", type(person))

# 10. Show ID and Type together
a = 50
print("10. ID:", id(a))
print("    Type:", type(a))


# ---------- PART 2: Binary, Octal, Hexadecimal Conversion ----------

# 11. Convert decimal to binary
n = 15
print("11. Binary of", n, "is", bin(n))

# 12. Convert decimal to octal
n = 25
print("12. Octal of", n, "is", oct(n))

# 13. Convert decimal to hexadecimal
n = 255
print("13. Hexadecimal of", n, "is", hex(n))

# 14. Convert binary to decimal
b = "0b1101"
decimal = int(b, 2)
print("14. Decimal =", decimal)

# 15. Convert octal to decimal
o = "0o17"
decimal = int(o, 8)
print("15. Decimal =", decimal)

# 16. Convert hexadecimal to decimal
h = "0xff"
decimal = int(h, 16)
print("16. Decimal =", decimal)

# 17. Print
