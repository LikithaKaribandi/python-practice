def get_grade(score):
    if score >= 90:
        return "A"
    elif score >= 60:
        return "B"
    else:
        return "C"

def analyse(marks):
    for subject, score in marks.items():
        print(subject, "=", score, "Grade:", get_grade(score))

    total = sum(marks.values())
    average = total / len(marks)

    print("Total:", total)
    print("Average:", round(average, 2))
    print("Highest subject:", max(marks, key=marks.get))
    print("Lowest subject:", min(marks, key=marks.get))

    if average >= 60:
        print("Result: Pass")
    else:
        print("Result: Fail")

