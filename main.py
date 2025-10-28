# main.py
from student import Student
from file_ops import save_data, load_data
from utils import get_marks

def add_student(students):
    sid = input("Enter Student ID: ")
    name = input("Enter Name: ")
    marks = get_marks()
    students.append(Student(sid, name, marks))
    print("Student added successfully!\n")

def view_students(students):
    if not students:
        print("No student records found.\n")
    for s in students:
        s.display()
    print()

def update_marks(students):
    sid = input("Enter Student ID to update: ")
    for s in students:
        if s.id == sid:
            subject = input("Enter subject to update: ")
            try:
                new_mark = int(input("Enter new mark: "))
                if 0 <= new_mark <= 100:
                    s.update_mark(subject, new_mark)
                    print("Marks updated successfully!\n")
                else:
                    print("Invalid mark range!\n")
            except ValueError:
                print("Please enter a valid number!\n")
            return
    print("Student not found!\n")

def main():
    students = load_data()
    while True:
        print("📚 Student Management System")
        print("1. Add Student\n2. View Students\n3. Update Marks\n4. Save Data\n5. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            add_student(students)
        elif choice == '2':
            view_students(students)
        elif choice == '3':
            update_marks(students)
        elif choice == '4':
            save_data(students)
        elif choice == '5':
            save_data(students)
            print("Exiting... Goodbye! 👋")
            break
        else:
            print("Invalid choice, try again.\n")

if __name__ == "__main__":
    main()
