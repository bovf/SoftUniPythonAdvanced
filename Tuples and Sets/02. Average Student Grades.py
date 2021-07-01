number_of_students = int(input())

class_students = {}
for _ in range(number_of_students):
    student_grade = input().split()
    student = student_grade[0]
    grade = float(student_grade[1])
    if student not in class_students:
        class_students[student] = []
    class_students[student].append(grade)


for name in class_students.keys():
    grade_average = 0.0
    grade_sum = 0
    for grades in class_students[name]:
        grade_sum += grades
    grade_average = grade_sum / len(class_students[name])
    print(f"{name} -> {' '.join(map('{:.2f}'.format, (class_students[name])))} (avg: {grade_average:.2f})")
