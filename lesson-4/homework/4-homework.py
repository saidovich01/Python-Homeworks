# Task-1
dictionary = {5: 'a', 40: 'b', 15: 'c', 50: 'd', 30: 'e', 100: 'f', 80: 'g', 150: 'h'}

sorted_dict1 = dict(sorted(dictionary.items(), reverse=True))
sorted_dict2 = dict(sorted(dictionary.items(), reverse=False))

print(sorted_dict1)
print(sorted_dict2)



# Task-2
Numbers = {0: 10, 1: 20}
Numbers.update([(2 , 30)])
print(Numbers)

# Task-3
dic1 = {1: 10, 2: 20}
dic2 = {3: 30, 4: 40}
dic3 = {5: 50, 6: 60}

dic1.update(dic2)
dic1.update(dic3)
print(dic1)

# Task-4
n = 5
print({x: x*x for x in range(1, n+1)})

# Task-5
n = 15
print({x: x**2 for x in range(1, n+1)})



# Set Exercise-1
list = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5]
set = set(list)
print(set)

# Set Exercise-2
Set = {1, 5, 10, 15, 20, 25}
for item in Set:
    print(item)

# Set Exercise-3
Set = {1, 5, 10, 15, 20, 25}
Set.add(30)
print(Set)
Set.update([35, 40, 45, 50])
print(Set)

# Set Exercise-4
Set = {1, 5, 10, 15, 20, 25}
Set.remove(15)
print(Set)

# Set Exercise-5
Set = {1, 5, 10, 15, 20, 25}
Num = int(input("enter the Num: " ))
if Num in Set:
    Set.remove(Num)
print(Set)

