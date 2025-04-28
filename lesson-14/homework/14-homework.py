# Task-1
import json
with open("students.json", "r", encoding="utf-8") as file:
    students = json.load(file)
    print(students)

    for item in students:
        print(item["name"])
        print(item["age"])
        print(item["subject"])


# Task-2

import requests
import json

url = "http://api.openweathermap.org/data/2.5/weather?lat=41.3123363&lon=69.2787079&appid=4c64ec380eda4ba57ee01de480f290b4&units=metric"


data = requests.get(url)

json_data = data.json()

print(json_data)
with open("weather.json", "w", encoding="utf-8") as file:
    json.dump(json_data, file, indent=4)

with open("weather.json", "r", encoding="utf-8") as file:
    weather = json.load(file)

for item in weather["main"]:
    print(item)
    



# Task-4
import requests
import json

url = "https://www.omdbapi.com/?i=tt3896198&apikey=f14f3a10"


data = requests.get(url)

json_data = data.json()

print(json_data)
with open("omdp.json", "w", encoding="utf-8") as file:
    json.dump(json_data, file, indent=4)

with open("omdp.json", "r", encoding="utf-8") as file:
    omdp = json.load(file)

for item in omdp["Ratings"]:
    print(item)
