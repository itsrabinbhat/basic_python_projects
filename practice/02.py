'''Print the average of the marks array for the student name provided, showing 2 places after the decimal.'''
students_marks = {
    "Krishna" : [67,68,69],
    "Arjun" : [70,98,63],
    "Malika" : [52,56,60]
}
query_name = input("Enter a name: ")
avg_marks = None

for key in students_marks:
    if key.upper() == query_name.upper():
        avg_marks = sum(students_marks[key]) / len(students_marks[key])

print("{:.2f}".format(avg_marks))
