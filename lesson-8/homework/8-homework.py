# Exception Handling Exercises
# 1. ZeroDivisionError
try:
    num = 10
    print(num / 0)
except ZeroDivisionError:
    print("Nolga bolish mumkin emas.")

# 2. ValueError
try:
    number = int(input("Butun son kiriting: "))
except ValueError:
    print("Xato: Butun son kiriting.")

# 3. FileNotFoundError
try:
    with open('non_existent_file.txt') as f:
        print(f.read())
except FileNotFoundError:
    print("Fayl topilmadi.")

# 4. TypeError
try:
    a = input("1-son: ")
    b = input("2-son: ")
    print(float(a) + float(b))
except ValueError:
    raise TypeError("Faqat raqam kiriting.")

# 5. PermissionError
try:
    with open('/root/secret.txt') as f:
        print(f.read())
except PermissionError:
    print("Ruxsat yo‘q.")

# 6. IndexError
try:
    lst = [1, 2, 3]
    print(lst[10])
except IndexError:
    print("Index mavjud emas.")

# 7. KeyboardInterrupt
try:
    num = input("Son kiriting: ")
except KeyboardInterrupt:
    print("\nKiritish bekor qilindi.")

# 8. ArithmeticError
try:
    result = 1 / 0
except ArithmeticError:
    print("Aritmetik xato yuz berdi.")

# 9. UnicodeDecodeError
try:
    with open('test.txt', encoding='ascii') as f:
        print(f.read())
except UnicodeDecodeError:
    print("Kodlash xatosi.")

# 10. AttributeError
try:
    lst = [1, 2, 3]
    lst.push(4)
except AttributeError:
    print("Bunday atribut mavjud emas.")


#################################################################################
# Python file input/output
# 1. Read entire file
with open("sample.txt") as f:
    print(f.read())

# 2. Read first n lines
n = 3
with open("sample.txt") as f:
    for i in range(n):
        print(f.readline())

# 3. Append text and display

# 4. Read last n lines

# 5. Store lines in list
with open("sample.txt") as f:
    lines = f.readlines()
print(lines)

# 6. Store lines in variable
with open("sample.txt") as f:
    text = f.read()
print(text)

# 7. Store lines into array
with open("sample.txt") as f:
    array = [line.strip() for line in f]
print(array)

# 8. Find longest words
with open("sample.txt") as f:
    words = f.read().split()
    longest = max(words, key=len)
print("Eng uzun soz:", longest)

# 9. Count number of lines
with open("sample.txt") as f:
    print(len(f.readlines()))

# 10. Word frequency

# 11. File size
import os
print(os.path.getsize("sample.txt"))

# 12. Write list to file
lst = ["hello", "world"]
with open("output.txt", "w") as f:
    for item in lst:
        f.write(item + "\n")

# 13. Copy file content
with open("sample.txt") as src, open("copy.txt", "w") as dst:
    dst.write(src.read())

# 14. Combine line by line

# 15. Read random line


# 16. File closed check
f = open("sample.txt")
print(f.closed)
f.close()
print(f.closed)

# 17. Remove newline characters
with open("sample.txt") as f:
    content = f.read().replace("\n", "")
print(content)

# 18. Word count (with commas)
with open("sample.txt") as f:
    text = f.read().replace(",", " ")
    print(len(text.split()))

# 19. Extract characters from multiple files

# 20. Generate 26 text files A-Z

# 21. Alphabet with fixed letters per line


