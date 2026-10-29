# Program 1: Print a list
numbers = [1, 2, 3, 4, 5]
print(numbers)
print(numbers[0])
print(numbers[-1])
print(len(numbers))

# Program 2: Sum and average
numbers = [1, 2, 3, 4, 5]
total = sum(numbers)
average = total / len(numbers)
print("Sum:", total)
print("Average:", average)

# Program 3: Largest and smallest
marks = [85, 67, 78, 93, 45]
print("Highest marks:", max(marks))
print("Lowest marks:", min(marks))

# Program 4: Sort three numbers
a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
c = float(input("Enter third number: "))
num = [a, b, c]
num.sort()
print("Sorted numbers:", num)

# Program 5: Tuple practice
me = ("honey", 22, "iiit")
print("Name:", me[0])
print("Age:", me[1])
print("College:", me[2])
print("Number of items:", len(me))
