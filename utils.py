# utils.py
def get_marks():
    marks = {}
    subjects = ('Math', 'Science', 'English')  # Tuple (immutable)
    for sub in subjects:
        while True:
            try:
                m = int(input(f"Enter marks for {sub}: "))
                if 0 <= m <= 100:
                    marks[sub] = m
                    break
                else:
                    print("Marks must be between 0 and 100.")
            except ValueError:
                print("Enter a valid number.")
    return marks
