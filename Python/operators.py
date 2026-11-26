
# Program to demonstrate different operators

a = 10
b = 5

# 1. Arithmetic Operators
print("ARITHMETIC OPERATORS")
print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)
print("Modulus:", a % b)
print("Exponent:", a ** b)
print("Floor Division:", a // b)

# 2. Relational Operators
print("\nRELATIONAL OPERATORS")
print("Equal:", a == b)
print("Not Equal:", a != b)
print("Greater Than:", a > b)
print("Less Than:", a < b)
print("Greater Than or Equal:", a >= b)
print("Less Than or Equal:", a <= b)

# 3. Logical Operators
print("\nLOGICAL OPERATORS")
print("AND:", a > 5 and b < 10)
print("OR:", a < 5 or b < 10)
print("NOT:", not(a > b))

# 4. Membership Operators
print("\nMEMBERSHIP OPERATORS")
numbers = [10, 20, 30, 40]
print("10 in numbers:", 10 in numbers)
print("50 not in numbers:", 50 not in numbers)

# 5. Identity Operators
print("\nIDENTITY OPERATORS")
x = [1, 2, 3]
y = x
z = [1, 2, 3]

print("x is y:", x is y)
print("x is z:", x is z)
print("x is not z:", x is not z)
