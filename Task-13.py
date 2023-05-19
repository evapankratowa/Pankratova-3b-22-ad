class Car:
    def __init__(self, mark, model, age, price):
        self.mark = mark
        self.model = model
        self.age = age
        self.price = price

    def print_info(self):
        print(f'{self.mark} - {self.model}, год выпуска: {self.age}, цена: {self.price}')
