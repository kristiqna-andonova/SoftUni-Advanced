lines = int(input())
students = {}

for _ in range(lines):
    student_info = tuple(input().split())
    student, grade = student_info
    if student not in students:
        students[student] = []
    students[student].append(float(grade))

for student, grades in students.items():
    average_grade = sum(students[student]) / len(students[student])
    print(f"{student} -> {' '.join([f'{x:.2f}' for x in grades])} (avg: {average_grade:.2f})")
