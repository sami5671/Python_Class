def student_grades(students):
    # Calculate total manually
    total = 0
    for mark in students.values():
        total = total + mark

    # Find highest marks manually
    highest = 0
    for mark in students.values():
        if mark > highest:
            highest = mark

    # Find topper(s)
    toppers = []
    for name in students:
        if students[name] == highest:
            toppers.append(name)

    average = total / n
    print(f"\nAverage Marks: {average:.2f}")
    print("Top Scorer(s):", ", ".join(toppers))


students = {}
n = int(input("Enter number of students: "))

for i in range(n):
    name = input(f"Enter name of student {i + 1}: ")
    marks = float(input(f"Enter marks of {name}: "))
    students[name] = marks
# Run the function
student_grades(students)
