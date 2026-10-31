# Problem 1: Remove duplicates
numbers = [5, 3, 5, 2, 3, 1]
unique = sorted(set(numbers))
print(unique)

# Problem 2: Count unique
numbers = [10, 20, 10, 30, 20, 40]
unique = set(numbers)
print("Unique values:", unique)
print("Count of unique values:", len(unique))

# Problem 3: Common items
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}
print("Common items:", a & b)

# Problem 4: Missing items
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}
print("In a but not in b:", a - b)
print("In b but not in a:", b - a)

# Problem 5: Membership
subjects = {"maths", "physics", "chemistry", "biology", "english"}
print("maths" in subjects)      # True
print("history" in subjects)    # False

# Problem 1: Greeting
def greet(name):
    print("Hello,", name + "! Welcome.")

greet("Priya")
greet("Ravi")

# Problem 2: Add two numbers
def add(x, y):
    return x + y

result = add(5, 6)
print("Sum:", result)
print("Double the sum:", result * 2)

# Problem 3: Even or odd
def is_even(n):
    if n % 2 == 0:
        return True
    else:
        return False

print(is_even(4))   # True
print(is_even(7))   # False
print(is_even(0))   # True

# Problem 4: Find max without max()
def find_max(numbers):
    biggest = numbers[0]
    for n in numbers:
        if n > biggest:
            biggest = n
    return biggest

print(find_max([3, 9, 2, 7]))      # 9
print(find_max([-5, -2, -9]))      # -2
print(find_max([4]))               # 4

# Problem 5: Grade function
def get_grade(marks):
    if marks >= 90:
        return "A"
    elif marks >= 60:
        return "B"
    else:
        return "C"

print(get_grade(95))    # A
print(get_grade(90))    # A
print(get_grade(75))    # B
print(get_grade(60))    # B
print(get_grade(40))    # C
