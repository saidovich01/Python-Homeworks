# Task-1
class Circle:
    def __init__(self):
        pass
        
    def Area(self, radius):
        return 3.14 * radius ** 2

    def Lenght(self, radius):
        return 2 * 3.14 * radius

result = Circle()
print(result.Area(5))
print(result.Lenght(5))

# Task-2
from datetime import datetime

class Person:
    def __init__(self, name, country, date_of_birth):
        self.name = name
        self.country = country
        self.date_of_birth = datetime.strptime(date_of_birth, "%Y-%m-%d")

    def get_age(self):
        today = datetime.today()
        age = today.year - self.date_of_birth.year
        if (today.month, today.day) < (self.date_of_birth.month, self.date_of_birth.day):
            age -= 1
        return age


person1 = Person("Ali", "Uzbekistan", "1990-05-15")
print(f"{person1.name} from {person1.country} is {person1.get_age()} years old.")


# Task-3
class Calculator:

    def __init__(self):
        pass

    def qoshish(self, a, b):
        return a + b
    
    def ayirish(self, a, b):
        return a - b
    
    def bolish(self, a, b):
        return a/ b
    
    def kopaytirish(self, a, b):
        return a * b
    
result = Calculator()

print(result.ayirish(5, 2))



# Task-4
import math

class Shape:
    def area(self):
        pass

    def perimeter(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

    def perimeter(self):
        return 2 * math.pi * self.radius

class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side ** 2

    def perimeter(self):
        return 4 * self.side

class Triangle(Shape):
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def perimeter(self):
        return self.a + self.b + self.c

    def area(self):
        s = self.perimeter() / 2
        return math.sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))


# Task-8
class ShoppingCart:
    def __init__(self):
        self.items = {}

    def add_item(self, item, price):
        self.items[item] = self.items.get(item, 0) + price

    def remove_item(self, item):
        if item in self.items:
            del self.items[item]

    def total_price(self):
        return sum(self.items.values())


class ShoppingCart:
    def __init__(self):
        self.items = {}

    def add_item(self, item, price):
        self.items[item] = self.items.get(item, 0) + price

    def remove_item(self, item):
        if item in self.items:
            del self.items[item]

    def total_price(self):
        return sum(self.items.values())

# Task-11
class Customer:
    def __init__(self, name, account_number, balance=0.0):
        self.name = name
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited ${amount:.2f} to {self.name}'s account.")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if amount > 0:
            if self.balance >= amount:
                self.balance -= amount
                print(f"Withdrew ${amount:.2f} from {self.name}'s account.")
            else:
                print("Insufficient balance!")
        else:
            print("Withdrawal amount must be positive.")

    def display_balance(self):
        print(f"{self.name}'s account balance: ${self.balance:.2f}")

class Bank:
    def __init__(self):
        self.customers = {}

    def add_customer(self, name, account_number, initial_balance=0.0):
        if account_number in self.customers:
            print("Account number already exists.")
        else:
            self.customers[account_number] = Customer(name, account_number, initial_balance)
            print(f"Customer {name} added with account number {account_number}.")

    def deposit(self, account_number, amount):
        customer = self.customers.get(account_number)
        if customer:
            customer.deposit(amount)
        else:
            print("Customer not found.")

    def withdraw(self, account_number, amount):
        customer = self.customers.get(account_number)
        if customer:
            customer.withdraw(amount)
        else:
            print("Customer not found.")

    def display_customer_balance(self, account_number):
        customer = self.customers.get(account_number)
        if customer:
            customer.display_balance()
        else:
            print("Customer not found.")




