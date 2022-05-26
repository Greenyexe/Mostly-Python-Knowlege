# sort() method = used with lists
# sort() function = used with iterables

#students = ["Bruno", "Laurie", "Luke", "Fin", "Ben", "Douglas"]

#students.sort()

#students.sort(reverse=True)

#sortedStudents = sorted(students, reverse=True)

#for i in students:
#    print(i)
#for i in sortedStudents:
#    print(i)





students = [("Bruno", "A*", 14),
                    ("Laurie", "F", 14),
                    ("Ben", "B", 17),
                    ("Luke", "C-", 15),
                    ("Douglas", "D", 13)]

grade = lambda grades:grades[1]
#students.sort(key=grade, reverse=True)
sorted_students = sorted(students, key=grade)

for i in sorted_students:
    print(i)