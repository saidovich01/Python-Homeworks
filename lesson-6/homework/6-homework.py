# Task-1

txt = input("Enter the word:")

for index, letter in enumerate(txt, start=1):
    print(index, letter)


# Task-2

n = int(input("Enter the num : "))

for i in range(0, n):
    print(i**2)


# Task-3
# Exercise-1
a = 1
while a <= 10:
    print(a)
    a += 1

# Exercise-2  
for i in range(1, 6):
    for n in range(1, i + 1):
        print(n , end=" ")
    print()

# Exercise-3
num = int(input("Enter the num : "))
total = sum(range(1, num + 1))
print("Sum is :", total)

# Exercise-4
num = int(input("Enter the num : "))
for i in range(1, 11):
    print(i * num)

# Exercise-5
numbers = [12, 75, 150, 180, 145, 525, 50]

for num in numbers:
    if num in [75, 150, 145]:
        print(num)

# Exercise-6
num = int(input("Enter the num :"))
print(len(str(num)))

# Exercise-7
n = 5
for i in range(n, 0, -1):
    for e in range(i, 0, -1):
        print(e , end=" ")
    print()

# Exercise-8
list1 = [10, 20, 30, 40, 50]
for n in reversed(list1):
    print(n)

# Exersise-9
for n in range(-10, 0):
    print(n)

# Exercise-10
for n in range(0, 5):
    print(n)
else:
    print("Done!")

# Exercise-11
for num in range(25, 50):
    for i in range(2, num):
        if num % i == 0:
            break
    else:
        print(num)

# Exercise-12
fib1, fib2 = 0, 1
for _ in range(10):
    print(fib1, end=" ")
    fib1, fib2 = fib2, fib1 + fib2
print()

# Exercise-13
def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n - 1)
    
a = factorial(5)
print(a)


# Task-4
list1 = list(input("enter the numbers : "))
list2 = list(input("enter the numbers : "))
result = []

for e in list1:
    if e not in list2:
        result.append(e)
for i in list2:
    if i not in list1:
        result.append(i)

print(result)    






