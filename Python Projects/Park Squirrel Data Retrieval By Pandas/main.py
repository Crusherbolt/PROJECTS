# with open("weather-data.csv") as data_file:
#     data = data_file.readlines()
#     print(data)

# import csv
#
# with open("weather-data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     for row in data:
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))
#     print(temperatures)

# import pandas
#
# data = pandas.read_csv("weather-data.csv")
# print(type(data))
# print(type(data["temp"]))

# data_dict =data.to_dict()
# print(data_dict)

# templist = data["temp"].to_list()
# print(templist)
#
# average = sum(templist)/len(templist)
# print(average)
# SAME AS BELOW
# print(data["temp"].mean())
# print(data["temp"].max())
# print(data["temp"])
#
# Get Data in Columns
# print(data["condition"])
# print(data.condition)

# Get Data in Row
# print(data[data.day == "Monday"])
# print(data[data.temp == data.temp.max()])

# monday = data[data.day == "Monday"]
# monday_temp = int(monday.temp)
# monday_temp_F = monday_temp * 9/5 + 32
# print(monday_temp_F)

# Create a dataframe from Scratch
# data_dict = {
#     "students" : ["Amy","James","Vid"],
#     "scores" : [76,56,65]
# }
# data = pandas.DataFrame(data_dict)
# print(data)
# data.to_csv("new_data.csv ")

import pandas
data = pandas.read_csv("Central-Park-Squirrel-Census-Squirrel-Data.csv")
grey_squirrels_count = len(data[data["Primary Fur Color"] == "Gray"])
red_squirrels_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_squirrels_count = len(data[data["Primary Fur Color"] == "Black"])

data_dict = {
    "Fur Color" : ["Gray", "Cinnamon","Black"],
    "Count" : [grey_squirrels_count,red_squirrels_count,black_squirrels_count]
}

df =pandas.DataFrame(data_dict)
df.to_csv("squirrel.csv")