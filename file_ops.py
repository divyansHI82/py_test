# file_ops.py
import json

def save_data(students, filename="students.json"):
    data = [s.__dict__ for s in students]
    with open(filename, "w") as f:
        json.dump(data, f)
    print(" Data saved successfully!\n")

def load_data(filename="students.json"):
    try:
        with open(filename) as f:
            data = json.load(f)
        from student import Student
        return [Student(d['id'], d['name'], d['marks']) for d in data]
    except FileNotFoundError:
        print(" No saved data found, starting fresh.\n")
        return []
