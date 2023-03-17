# with open("weather_data.csv", mode="r") as sheet:
#     data = sheet.readlines()
#
# print(data)

# import csv
#
# with open("weather_data.csv") as sheet:
#     data = csv.reader(sheet)
#     next(data)
#     temperatures = []
#     for row in data:
#         temperatures.append(int(row[1]))
#         print(temperatures)
        # temperatures.append(int(row[1]))

import pandas

data = pandas.read_csv("weather_data.csv")
data_as_dict = data.to_dict()
print(data_as_dict)

temp_as_list = data["temp"].to_list()
print(temp_as_list)

# Calculates temperatures average using common Python methods
list_length = len(temp_as_list)
list_sum = sum(temp_as_list)
temp_average = list_sum / list_length
print(temp_average)

# Calculates temperatures average using Pandas methods
average = data["temp"].mean()
print(average)

temp_max = data["temp"].max()
print(temp_max)

# Select data column or row using Pandas
day = data.day
print(day)
monday = data[data.day == 'Monday']
print(monday)
max_temp = data.temp.max()
max_row = data[data.temp == max_temp]
print(max_row)

# Select Monday's temperature and convert it into Fahrenheit
monday_in_fahrenheit = monday.temp * 1.8 + 32
print(monday_in_fahrenheit)

# Create a DataFrame from scratch
data_dict = {
    "students": ["Amy", "James", "Angela"],
    "scores": [76, 56, 65]
}

data_as_df = pandas.DataFrame(data_dict)
data_as_df.to_csv("new_file.csv")
