import csv
import pandas

with open("weather_data.csv") as file:
    raw_datas = file.readlines()

print(raw_datas)
data = []
for r_data in raw_datas:
    content = r_data.strip("\n")
    data.append(content.split(","))

print(data)

# csv

with open("weather_data.csv") as data_file:
    data = csv.reader(data_file)
    temperatures = []
    for row in data:
        if row[1] != "temp":
            temperatures.append(int(row[1]))

print(temperatures)

# Pandas

data = pandas.read_csv("weather_data.csv")
print(data)
data_dict = data.to_dict()
print(data_dict)
temp_list = data["temp"].to_list()
temp_list_length = len(temp_list)
sum_temp = sum(temp_list)

avg_temp = sum_temp / temp_list_length
print(avg_temp)
avg_temp = data["temp"].mean()
print(avg_temp)
max_temp = data["temp"].max()
print(max_temp)

# Get Data in Columns
print(data.condition)

# Get Data in Row
print(data[data.day == "Monday"])
print(data[data.temp == max_temp])

monday = data[data.day == "Monday"]
print(monday.condition)
temp_celsius = monday.temp
temp_fahrenheit = temp_celsius * 1.8 + 32
print(temp_fahrenheit)

# Create a dataframe from scratch
data_dict = {
    "students": ["Amy", "James", "Angela"],
    "scores": [76, 56, 65]
}
csv_data = pandas.DataFrame(data_dict)
print(csv_data)
csv_data.to_csv("new_data.csv")
