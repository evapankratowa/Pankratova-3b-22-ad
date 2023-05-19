class Dog:
    def __init__(self, name, breed, age):
        self.name = name
        self.breed = breed
        self.age = age

    def dog_info(self):
        print(f'Имя: {self.name}, порода: {self.breed}, возраст: {self.age}')

doge = Dog('Хатико', 'шиба', '10')
doge.dog_info()