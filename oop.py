
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def greeting(self, guest_name):
        print(f"Hello {guest_name} I'm {self.name}, your assistant here to guide you.")

class BankAccount:
    def __init__(self, balance: float):
        self.balance = balance
    
    def deposit(self, amount: float):
        self.balance += amount

    def show_balance(self):
        print(f"Balance: ${self.balance:.2f}")


if __name__ == '__main__':
    s1 = Student('Jay', 25)
    print(s1.name)

    s1.greeting('Vee')
    print()

    acc = BankAccount(1000)
    acc.deposit(500)
    acc.show_balance()

