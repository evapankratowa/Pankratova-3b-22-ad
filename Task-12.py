class Student:
    def __init__(self, name, last_name, age, speciality):
        self.name = name
        self.last_name = last_name
        self.age = age
        self.speciality = speciality

    def print_info(self):
        print(f' {self.name} - {self.last_name}, возраст {self.age} лет, специальность {self.speciality}')
