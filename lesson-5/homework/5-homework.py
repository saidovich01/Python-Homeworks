# Task-1
year = int(input("Enter the year: "))

if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
    print("True")
else:
    print("False")

# Task-2
n = int(input("enter the num in range (1, 100):"))

if n % 2 == 1:
    print("Weird")
elif n % 2 == 0 and n in range (2, 6):
    print("Not Weird")
elif n % 2 == 0 and n in range (6, 21):
    print("Weird")
elif n % 2 == 0 and 20 < n <= 100:
    print("Not Weird")
else: 
    print("Invalid Number!")

# Task-3
a = int(input("a = "))
b = int(input("b = "))


if a % 2 != 0:
    a = a + 1
if b % 2 != 0:
    b = b - 1
if a > b:
    result = []
else:
    result = list(range(a, b + 1, 2))

print(result)

