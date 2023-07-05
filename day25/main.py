# with open("weather_data.csv") as weatherData:
#     data = weatherData.readlines()
#
# import csv
# with open("weather_data.csv") as weatherData:
#     data = csv.reader(weatherData)
#     temperatures = [row[1] for row in data]
#
#     for row in data:
#         print(row) #issue here as the data has already been read it cant read it again
#
#     print(temperatures)
#
# import csv
#
# with open("weather_data.csv") as weatherData:
#     data = csv.reader(weatherData)
#     data_rows = list(data)  # Store the rows in a list
#
#     temperatures = [int(row[1]) for row in data_rows[1:]]
#     print(temperatures)
#
#     for row in data_rows:
#         print(row)
#
# import pandas
# data = pandas.read_csv("weather_data.csv")
# print(data)

# import pandas
# data = pandas.read_csv("weather_data.csv")
# print(type(data))
# print(type(data["temp"]))
# data_dict = data.to_dict()
# print(data_dict)
# temperatures = data["temp"].to_list()
# print(temperatures)
# print(data.groupby("condition")["temp"].mean())
# print(data["temp"].mean())
# print(data["temp"].max())
# print(data.condition)
# print(data[data.day == "Monday"])
# print(data[data.temp == data.temp.max()])
# print(data[data.day == "Monday"].condition)
# print(f"{data[data.day == 'Monday'].temp.sum()}")
# print(f"{data[data.day == 'Monday'].temp.sum() * (9/5) + 32}")
#
# data_dict = {
#     "students": ["Jared", "Danell", "Hannah"],
#     "scores": ["98", "99", "76"]
# }
#
# data = pandas.DataFrame(data_dict)
# data.to_csv("new_data.csv")


import pandas

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
fur_counts = data.groupby(["Primary Fur Color"])["Primary Fur Color"].count()
fur_counts.to_csv("squirrel_count.csv")
print(fur_counts)