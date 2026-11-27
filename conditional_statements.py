
# Program to demonstrate Conditional Statements

# 1. Simple if
a = 10

if a > 0:
    print("Positive number")

# 2. if-else
b = 5

if b % 2 == 0:
    print("Even number")
else:
    print("Odd number")

# 3. if-elif-else
marks = 75

if marks >= 90:
    print("Grade A")
elif marks >= 70:
    print("Grade B")
else:
    print("Grade C")

# 4. Nested if
age = 20

if age >= 18:
    if age >= 21:
        print("Eligible")
    else:
        print("Not eligible yet")
else:
    print("Below 18")
