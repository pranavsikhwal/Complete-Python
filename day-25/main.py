# with open("weather_data - Sheet1 (1).csv",mode = "r")as file:
#     file_list = file.readlines()
#     print(file_list)
# import csv
# with open("weather_data - Sheet1 (1).csv",mode = "r")as file:
#     file_content = csv.reader(file)
#     temperature = []
#     for x in file_content:
#         if x[1] != "temp":
#             temperature.append(int(x[1]))
#         print(x)
#     print(temperature)

# import pandas
# data = pandas.read_csv("weather_data - Sheet1 (1).csv")
# print(data)
# print(data["temp"])
#
# data_dict = data.to_dict()
# print(data_dict)
# data_list = data["temp"].to_list()
# print(data_list)
# print(len(data_list))
# # sum_list = 0
# # for item in data_list:
# #     sum_list += item
# #print(sum(data_list)/7.0)
# print(data["temp"].mean())
# print(data["temp"].max())
# print(data[data.day == "Monday"])
#
# data_frame = {
#     "Students" : ["Rajesh","Ram","Lakhan"],
#     "Marks" : [10,23,45]
# }
# my_dataframe = pandas.DataFrame(data_frame)
# print(my_dataframe)
# my_dataframe.to_csv("DataFrame.csv ")

# import pandas
# data = pandas.read_csv("squarrel.csv")
# gray = len(data[data["Primary Fur Color"] == "Gray"])
# red = len(data[data["Primary Fur Color"] == "Cinnamon"])
# black = len(data[data["Primary Fur Color"] == "Black"])
# print(gray,red,black)
#
# dict = {
#     "Color":["Gray","Cinnamon","Black"],
#     "Count":[gray,red,black]
# }
# df = pandas.DataFrame(dict)
# print(df)
#
# df.to_csv("squirel.csv")
# #dataframe is 2-d and series is 1-d