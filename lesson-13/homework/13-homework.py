# Task-1
from datetime import datetime

birth_date = input("Enter your birth date : ")

def calculate_age(birth_date):
    birth_date = datetime.strptime(birth_date, "%Y-%m-%d")

    today = datetime.today()
    age = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))
    return age

calculate_age(birth_date)
print(f"Your age is : {calculate_age(birth_date)}")

# Task-2
from datetime import datetime
birth_date = input("Enter your birth date : ")

def calculate_days(birth_date):
    birth_date = datetime.strptime(birth_date, "%Y-%m-%d")
    today = datetime.today()
    days = today.year + 1 
    return days

calculate_days(birth_date)
print(f"Your days is : {calculate_days(birth_date)}")

# Task-3
from datetime import datetime, timedelta

def schedule_meeting():
    current_str = input("Enter the current date and time (YYYY-MM-DD HH:MM): ")
    hours = int(input("Meeting duration hours: "))
    minutes = int(input("Meeting duration minutes: "))

    current_time = datetime.strptime(current_str, "%Y-%m-%d %H:%M")
    end_time = current_time + timedelta(hours=hours, minutes=minutes)

    print(f"Meeting will end at: {end_time}")

schedule_meeting()

# Task-8
def check_password_strength():
    password = input("Enter your password: ")
    strength = "Weak"

    if (len(password) >= 8 and
        any(c.isupper() for c in password) and
        any(c.islower() for c in password) and
        any(c.isdigit() for c in password)):
        strength = "Strong"
    elif len(password) >= 6:
        strength = "Medium"

    print(f"Password strength: {strength}")

check_password_strength()

# Task-9
def find_word():
    text = input("Enter a block of text: ")
    word = input("Enter word to find: ").lower()
    words = text.lower().split()
    print(f"The word '{word}' is found")




