class Student:
    def __init__(self, name, last_name, grade, marks):
        self.name = name
        self.last_name = last_name
        self.grade = grade
        self.marks = marks

    def average_mark(self):
        return sum(self.marks) / len(self.marks)
