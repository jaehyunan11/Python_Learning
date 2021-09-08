# with open("weather_data.csv") as data_file:
#     data = data_file.readlines()
#     print(data)

import csv
import pandas as pd

# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     for row in data:
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))
#     print(temperatures)

data = pd.read_csv("weather_data.csv")

# DataFrame

# print(type(data))

# Series ( Columns in the excel)
# print(type(data['temp']))


# data_dict = data.to_dict()
# print(data_dict)
# temp_list = data["temp"].to_list()
# # print(sum(temp_list)/len(temp_list))
#
# print(data['temp'].mean())
# print(data['temp'].max())
# print(data['temp'].min())
#
#
# # Get data in Columns
#
# print(data["condition"])
# print(data.condition)

# Get data in Row
# print(data[data.day == "Monday"])
# print(data[data.temp == data.temp.max()])

# monday = data[data.day == "Monday"]
# monday_temp = int(monday.temp)
# monday_temp_F = monday_temp * 9/5 + 32
# print(monday_temp_F)

# Create a dataframe from scratch
# data_dict = {
#     "students": ["Amy", "James", "Angela"],
#     "scores": [76, 56, 65]
# }
# data = pd.DataFrame(data_dict)
# data.to_csv("new_data.csv")
