# Task-1
from datetime import datetime

class Task:
    def __init__(self, title, description, due_date):
        self.title = title
        self.description = description
        self.due_date = due_date
        self.completed = False

    def mark_complete(self):
        self.completed = True



class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def mark_complete(self, title):
        for task in self.tasks:
            if task.title == title:
                task.mark_complete()
                return f"Task '{title}' marked complete."
        return "Task not found."


# Task-2
class Post:
    def __init__(self, title, content, author):
        self.title = title
        self.content = content
        self.author = author



class Blog:
    def __init__(self):
        self.posts = []

    def add_post(self, post):
        self.posts.append(post)



# Task-3
class Account:
    def __init__(self, number, holder, balance=0):
        self.number = number
        self.holder = holder
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount > self.balance:
            return "Insufficient funds"
        self.balance -= amount
        return "Withdrawal successful"



class Bank:
    def __init__(self):
        self.accounts = {}

    def add_account(self, account):
        self.accounts[account.number] = account

    def get_account(self, number):
        return self.accounts.get(number, None)

    def check_balance(self, number):
        account = self.get_account(number)
        return f"Balance: ${account.balance:.2f}" if account else "Account not found"

    def transfer(self, from_num, to_num, amount):
        from_acc = self.get_account(from_num)
        to_acc = self.get_account(to_num)





