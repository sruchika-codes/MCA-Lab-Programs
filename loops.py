
# Program to demonstrate Looping Statements

# 1. For Loop
print("For Loop")
for i in range(1, 6):
    print(i)

# 2. While Loop
print("While Loop")
i = 1
while i <= 5:
    print(i)
    i += 1

# 3. Nested Loop
print("Nested Loop")
for i in range(1, 4):
    for j in range(1, 4):
        print(i, j)

# 4. Break Statement
print("Break Statement")
for i in range(1, 6):
    if i == 4:
        break
    print(i)

# 5. Continue Statement
print("Continue Statement")
for i in range(1, 6):
    if i == 3:
        continue
    print(i)

# 6. Pass Statement
print("Pass Statement")
for i in range(1, 4):
    if i == 2:
        pass
    print(i)
