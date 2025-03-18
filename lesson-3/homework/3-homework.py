# Task-1
Fruits = ["apple", "pear", "banana", "mango", "orange"]
print(Fruits[2])

# Task-2
num1 = [1, 5, 10, 15, 20]
num2 = [2, 25, 50, 75, 100]
num1.extend(num2)
print(num1)

# Task-4
Movies = ["Avengers ", "Dune", "Hobbits", "Harry Potter", "DC League"]
Movies_tup = tuple(Movies)

print(Movies_tup)

# Task-5
Cities = ["London", "Paris", "Rome", "Madrid", "Berlin"]

if "Paris" in Cities :
    print("Paris")


# Task-6
Num_List = [1, 5, 10, 15, 20]
Num_List.extend(Num_List)
print(Num_List)

# Task-7
Num_List = [1, 5, 10, 15, 20]
first, last = Num_List[0], Num_List[-1]
Num_List[0], Num_List[-1] = last, first
print(Num_List)

# Task-8
Tuple = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
print(Tuple[3:8])

# Task-9
Colors = ["red", "blue", "green", "white", "black", "blue"]
print(Colors.count("blue"))

# Task-10
animals = ("zebra", "tiger", "elephant", "giraffe", "lion", "cheetah", "bear", "wolf")
print(animals.index("lion"))

# Task-11
tuple1 = (1, 2, 3, 4, 5)
tuple2 = (6, 7, 8, 9, 10)
tuple1 += tuple2

print(tuple1)

# Task-12
my_list = [1, 2, 3, 4, 5, 6, 7, 8]
my_tuple = (10, 20, 30, 40, 50, 60)

print("Lenght of List: ", len(my_list))
print("Lenght of tuple:", len(my_tuple))

# Task-13
tuple = (10, 20, 30, 40, 50)
print(list(tuple))

# Task-14
tuple = (10, 20, 30, 40, 50)
print("max: ", max(tuple))
print("min: ", min(tuple))

# Task-15
animals = ("zebra", "tiger", "elephant", "giraffe", "lion", "cheetah", "bear", "wolf")
print(animals[::-1])



