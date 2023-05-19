class BankAccount:
    def __init__(self, name, number, balance):
        self.name = name
        self.number = number
        self.balance = balance

    def withdraw_funds(self, amount):
        self.balance -= amount
        print(f'{self.name}, Вы сняли {amount} рублей. Остаток на счете: {self.balance}')

    def top_up_funds(self, amount):
        self.balance += amount
        print(f'{self.name}, Вы пополнили счет на {amount} рублей. Остаток на счете: {self.balance}')
