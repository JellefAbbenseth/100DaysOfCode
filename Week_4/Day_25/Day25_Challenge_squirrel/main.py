# Challenge get the number of grey, red and black colored squirrels
import pandas

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
# print(data)
# data_column_fur_color = data["Primary Fur Color"]
# print(data_column_fur_color)
num_gray = len(data[data["Primary Fur Color"] == "Gray"])
num_red = len(data[data["Primary Fur Color"] == "Cinnamon"])
num_black = len(data[data["Primary Fur Color"] == "Black"])
# print(num_gray)
# print(num_red)
# print(num_black)

data_dict = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [num_gray, num_red, num_black]
}

csv_data = pandas.DataFrame(data_dict)
print(csv_data)
csv_data.to_csv("squirrel_count.csv")
