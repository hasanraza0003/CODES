import pandas as pd


data = pd.read_csv(r"F:\1JOURNEY_TO-INTERNSHIP\1PYTHON BOOTCAMP\GetFreeCourses.Co-Udemy-100 Days of Code The Complete Python Pro Bootcamp for 2023\25 - Day 25 Intermediate Working with CSV Data and the Pandas Library\229 - 2018-Central-Park-Squirrel-Census-Squirrel-Data.csv")

# SORT THE FILE DATA ACCORDING TO FUR COLOUR OF SQUIRREL

# method 1
# gray_colour = data[data["Primary Fur Color"] == "Gray"]
# x = gray_colour["Primary Fur Color"]
# gray_list = x.to_list()
# red_colour = data[data["Primary Fur Color"] == "Cinnamon"]
# y = red_colour["Primary Fur Color"]
# red_list = y.to_list()
# black_colour = data[data["Primary Fur Color"] == "Black"]
# z = black_colour["Primary Fur Color"]
# black_list = z.to_list()
# data_dict ={
#     "fur_color" : ["grey" , "red" , "black"],
#     "count" : [len(gray_list) ,len(red_list),len(black_list) ]
# }
# new_data = pd.DataFrame(data_dict)
# new_data.to_csv("color.csv")

# method 2
# gray_colour = len(data[data["Primary Fur Color"] == "Gray"])
# red_colour = len(data[data["Primary Fur Color"] == "Cinnamon"])
# black_colour = len(data[data["Primary Fur Color"] == "Black"])

# data_dict ={
#     "fur_color" : ["grey" , "red" , "black"],
#     "count" : [gray_colour,red_colour,black_colour ]
# }
# new_data_2 = pd.DataFrame(data_dict)
# new_data_2.to_csv("color_2.csv")
