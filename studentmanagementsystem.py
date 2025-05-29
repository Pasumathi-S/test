class student:
    def __init__(self, name, roll_no, marks):
        self.name = name
        self.roll_no = roll_no
        self.marks = marks

    def __str__(self):
            return f"Name:{self.name}, Roll No:{self.roll_no},Marks: {self.marks}"


students = []


def add_student(name, roll_no, marks):
    students.append(student(name, roll_no, marks))


def display_students():
    for s in students:
        print(s)


def highest_marks():
    top_student = max(students, key=lambda s: s.marks)
    print("Topper:", top_student)


add_student("John", 1, 95)
add_student("Lisa", 16, 88)
add_student("Luke", 5, 96)

display_students()
highest_marks()
