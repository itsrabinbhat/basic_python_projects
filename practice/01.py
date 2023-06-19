'''Print the name(s) of any student(s) having the second lowest grade in. If there are multiple students, order their names alphabetically and print each one on a new line'''

students = [["Harry", 37],["Berry",37],["Tina", 36],["Harsh",39],["Ram",38]]
marks = [students[i][1] for i in range(len(students))]

unique_marks = set(marks)
unique_marks = sorted(unique_marks)
second_high_score = unique_marks[1]

second_high = [students[i][0] for i in range(len(students)) if students[i][1] == second_high_score]
second_high.sort()
print(*second_high, sep='\n')