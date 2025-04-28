# Task-1
# Ex-53
import numpy as np
array = np.arange(1, 10)
print(type(array))
print(array.astype("int32"))


# Ex-54
import numpy as np

with open(f"Python-homeworks/num.txt", "r") as file:
    list = file.read()
    print(list)

    array = np.array(list)
    print(array)

    print(type(array))



##########################################################################################
# Task-2
import numpy as np

array = np.arange(1, 11)
print(array)

array2 = array ** 2
print(array2)

print(np.sum(array))
print(np.sum(array2))

print(np.mean(array))
print(np.mean(array2))

print(np.std(array2))
