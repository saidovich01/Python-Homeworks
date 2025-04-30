import math
# math_operation.py
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error: Division by zero"
    return a / b

# string.py
def reverse_string(s):
    return s[::-1]

def count_vowels(s):
    return sum(1 for char in s.lower() if char in "aeiou")



# geometry.py
def calculate_area(radius):
    return math.pi * radius ** 2

def calculate_circumference(radius):
    return 2 * math.pi * radius


# file.py
def read_file(file_path):
    with open(file_path, 'r') as file:
        return file.read()


def write_file(file_path, content):
    with open(file_path, 'w') as file:
        file.write(content)


# __init__.py
# Optionally expose read_file and write_file
from .file_reader import read_file
from .file_writer import write_file


# main.py
from math_operation import add, subtract
from string import reverse_string, count_vowels
from geometry import calculate_area, calculate_circumference
from file import read_file, write_file

