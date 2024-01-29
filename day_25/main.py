# with open("weather_data.csv") as file:
#     data = file.readlines()

# import csv

# with open("weather_data.csv") as file:
#     data = csv.reader(file)
#
#     temperatures = []
#     for row in data:
#         if row[1].isnumeric():
#             temperatures.append(int(row[1]))
#
#     print(temperatures)

import pandas

data = pandas.read_csv("weather_data.csv")
# print(data["temp"])

# data_dict = data.to_dict()
# print(data_dict)

# temp_list = data["temp"].to_list()
# print(temp_list)
# print(sum(temp_list) / len(temp_list))

# print(data["temp"].mean())

# print(data["temp"].max())

#data data in a row
# print(data[data.day == "Monday"])
# print(data[data.temp == data.temp.max()])

# def to_fahrenheit(temp):
#     return (temp * (9/5)) + 32
#
# monday = data[data.day == "Monday"]
# monday_temp = monday.temp[0]
# f_temp = to_fahrenheit(monday_temp)
# print(f"{monday_temp}C = {f_temp}F")

#Create a dataframe from scratch
data_dict = {
    "students": ["Amy", "James", "Angela"],
    "scores": [76, 56, 65]
}

data = pandas.DataFrame(data_dict)
data.to_csv("new_data.csv")
