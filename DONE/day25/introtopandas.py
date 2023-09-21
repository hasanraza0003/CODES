# import pandas

# x= pandas.read_csv(r"day25\227 - weather-data.csv")

# print(x)      ## to print whole csv file data

# x.to_dict()              # convert csv into dictionary
# x["temp"].to_list()      # convert csv into list


# #calculating average without using pandas
# temp = x["temp"].to_list()
# avg = sum(temp) / len(temp)
# print(avg)

# #calculating avg with using pandas 
# print(x["temp"].mean())

# #calculating max with using pandas
# print(x["temp"].max())
# # 
# #get data in columns
# print(x["condition"])
# print(x.condition)

# # get data in row
# print(x[x.day == "Monday"])
# #  * get the max temprature row from the data file 
# print(x[x.temp == x.temp.max()])

# # print monday temprature and converted into farenheit 
# y = x[x.day == "Monday"]
# c_to_f = (y.temp * (9/5))+32
# print(c_to_f)


# create a data_frame from scratch : 
# data_dict = {
#     "student": ["amy" , "james" , "angela"] ,
#     "scores" : [75,78,72]
# }

# data = pandas.DataFrame(data_dict)
# data.to_csv("new_data.csv")
# print(data)