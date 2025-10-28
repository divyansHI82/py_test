# student.py
class Student:
    def __init__(self, sid, name, marks):
        self.id = sid
        self.name = name
        self.marks = marks

    def update_mark(self, subject, new_mark):
        if subject in self.marks:
            self.marks[subject] = new_mark
        else:
            print("Subject not found!")

    def average(self):
        return sum(self.marks.values()) / len(self.marks)

    def display(self):
        print(f"ID: {self.id}, Name: {self.name}, Marks: {self.marks}, Avg: {self.average():.2f}")
