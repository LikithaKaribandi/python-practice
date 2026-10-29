# Program 1: Create and print
details = {"name": "priya", "age": 24, "college": "university"}
print(details["name"])
print(details.get("age"))
print(details["college"])

# Program 2: Add and update
details = {"name": "priya", "age": 24, "college": "university"}
details["city"] = "hyderabad"
details["age"] = 23
print("Updated details:", details)

# Program 3: Safe lookup
details = {"name": "priya", "age": 24, "college": "university"}
print(details.get("phone", "Not found"))

# Program 4: Marks total and average
marks = {"math": 87, "sci": 46, "phy": 67}
total = sum(marks.values())
average = total / len(marks)
print("Total marks:", total)
print("Average:", round(average, 2))

# Program 5: User-built dictionary
name = input("Enter name: ")
marks = float(input("Enter marks: "))
student = {"name": name, "marks": marks}
print(student)
