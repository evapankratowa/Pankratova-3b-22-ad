class Cat:
    def __init__(self, name, age, color):
        self.name = name
        self.color = color
        self.age = age

    def print_info(self):
        print(f'Кошка по имени- {self.name},  возраст {self.age} лет, цвет {self.color}')
