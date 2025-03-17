Task-1
Name = input("Name : ")
DoB = int(input("Year of Birth : "))
from datetime import datetime
CurrentYear = datetime.now().year
Age = CurrentYear - DoB

print(f"Name {Name} \nYear of Birth {DoB} \nAge {Age}")

Task-2
txt = 'LMaasleitbtui'
print(txt[0::2], txt[1::2])

Task-3
txt = 'MsaatmiazD'
print(txt[0::2], txt[10::-2])

Task-4
txt = "I'am John. I am from London"
print(txt[21:27])

Task-5
Text = input("Enter the any word: ")
Reversed = Text[::-1]
print(f"Text: {Text}\nReversed: {Reversed}")

Task-7
num_list = list(input("Enter the list of Number: ").split())
print("max value:", max(num_list))
