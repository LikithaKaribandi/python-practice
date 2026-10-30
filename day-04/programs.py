# Day 4: if/else and loops.

# Program 1: Positive, negative or zero
a = float(input("Enter a number: "))

if a > 0:
    print("Positive")
elif a < 0:
    print("Negative")
else:
    print("Zero")

# Program 2: Even or odd
a = int(input("Enter a number: "))

if a % 2 == 0:
    print("Even")
else:
    print("Odd")

# Program 3: Grade checker
marks = float(input("Enter marks: "))

if marks >= 90:
    print("Grade A")
elif marks >= 60:
    print("Grade B")
else:
    print("Grade C")

# Program 4: Print 1 to 10
for i in range(1, 11):
    print(i)

# Program 5: Sum of 1 to N
n = int(input("Enter N: "))
total = 0

for i in range(1, n + 1):
    total = total + i

print("Sum =", total)

# Program 6: Multiplication table
n = int(input("Enter a number: "))

for i in range(1, 11):
    print(n, "x", i, "=", n * i)
