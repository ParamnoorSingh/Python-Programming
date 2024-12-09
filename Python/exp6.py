# WAP to create a list of students record and search a student record using a dictionary

def students_record():
    students = []
    n = int(input("Enter the number of students: "))
    for i in range(n):
        student = {}
        student['id'] = input(f"Enter ID for student {i+1}: ")
        student['name'] = input(f"Enter name for student {i+1}: ")
        student['age'] = int(input(f"Enter the age for student {i+1}: "))
        student['grade'] = input(f"Enter grade for student {i+1}: ")
        students.append(student)
    return students

def search_student(students, search_id):
    for student in students:
        if student['id'] == search_id:
            return student
    return None


students = students_record()


print("\nAll student records:")
for student in students:
    print(student)


search_id = input("\nEnter the ID of the student to search for: ")
result = search_student(students, search_id)
if result:
    print("Student found:", result)
else:
    print("Student not found.")

