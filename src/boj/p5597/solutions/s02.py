def solution():
    students = [0] * 31

    for i in range(28):
        student_id = int(input())
        students[student_id] = 1

    for i, s in enumerate(students[1:], 1):
        if s == 0:
            print(i)
