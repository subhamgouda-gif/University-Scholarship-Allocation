students = [
    ("Asha", 92.4, [88, 91, 95], 94, 180000),
    ("Ravi", 89.8, [78, 84, 86], 91, 220000),
    ("Mina", 91.0, [91, 89, 93], 88, 260000),
    ("Dev", 92.4, [88, 91, 95], 96, 180000),
    ("Ira", 88.5, [70, 70, 72], 82, 120000),
]

minimum_average = 85
minimum_subject_mark = 70
minimum_attendance = 75
maximum_family_income = 250000
eligible_students = []

print("=" * 68)
print("UNIVERSITY SCHOLARSHIP ALLOCATION")
print("=" * 68)

for student in students:
    name, average, subject_marks, attendance, family_income = student
    subjects_passed = True

    for mark in subject_marks:
        if mark < minimum_subject_mark:
            subjects_passed = False

    if (average >= minimum_average and subjects_passed
            and attendance >= minimum_attendance
            and family_income <= maximum_family_income):
        eligible_students.append(student)

for first_index in range(len(eligible_students)):
    for second_index in range(first_index + 1, len(eligible_students)):
        first = eligible_students[first_index]
        second = eligible_students[second_index]
        should_swap = False

        if second[1] > first[1]:
            should_swap = True
        elif second[1] == first[1] and second[3] > first[3]:
            should_swap = True
        elif (second[1] == first[1] and second[3] == first[3]
                and second[4] < first[4]):
            should_swap = True
        elif (second[1] == first[1] and second[3] == first[3]
                and second[4] == first[4] and second[0] < first[0]):
            should_swap = True

        if should_swap:
            eligible_students[first_index], eligible_students[second_index] = (
                eligible_students[second_index], eligible_students[first_index]
            )

print("Eligibility: average >= 85, every subject >= 70, attendance >= 75%,")
print("and family income <= 250000.")
print("Tie-break order: average, attendance, lower income, then name.")
print("-" * 68)

if len(eligible_students) == 0:
    print("No students qualify for a scholarship.")
else:
    print("Rank  Student  Average  Attendance  Family income")
    rank = 1
    for student in eligible_students:
        name, average, subject_marks, attendance, family_income = student
        print(rank, name, average, attendance, family_income)
        rank = rank + 1

print("=" * 68)
