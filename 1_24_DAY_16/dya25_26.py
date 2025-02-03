import pandas as pd

# df = pd.read_csv("D:/SNEHA1/100_Day_of_code/23_1_DAY_15/weather_data.csv")
# print(df)
# # print(type(df))
# print(type(df["temp"]))

# data_dict=df.to_dict()
# print(data_dict)

# day_list=df["day"].to_list()
# print(day_list)
#
# temp_list=df["temp"].to_list()
# print(temp_list)
#
# #average or mean of sereis
# average_temp=sum(temp_list)/len(temp_list)
# print(average_temp)
#
# print(df["temp"].mean())
# print(df["temp"].max())
#
# #fatching spoecific coloumn
# print(df["condition"])
# print(df.condition)

# x= df[df.day == "Sunday"]
# print(x)
# print(df[df.temp == df.temp.max()])
# #
# monday = df[df.day == "Monday"]
# # print(monday.condition)
#
# f=(monday.temp[0] * (9/5))+ 32
# print(f)

# creating dataframe
#
# dict1 ={
#     "name":["fAZF","sdfgtzst","etawe","sdtgzs"],
#     "marks":[23,45,78,90]
# }
#
# data=pd.DataFrame(dict1)
# print(data)
# data.to_csv("new.csv")


# import pandas as pd
#
# df=pd.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
# gray_squirrel_count=len(df[df["Primary Fur Color"] == "Gray"])
# Cinnamon_squirrel_count=len(df[df["Primary Fur Color"] == "Cinnamon"])
# black_squirrel_count=len(df[df["Primary Fur Color"] == "Black"])
# print(Cinnamon_squirrel_count)
# print(gray_squirrel_count)
# print(black_squirrel_count)
#
# my_dict ={
#     "primary color":["Black","Gray","Cinnamon"],
#     "count":[black_squirrel_count,gray_squirrel_count,Cinnamon_squirrel_count]
#
# }
# print(my_dict)
#
# data=pd.DataFrame(my_dict)
# print(data)
# # data.to_csv("squirrel.csv")

# udemy day26
# list comprehension
# list1=[1,2,3]
# list2=[]
# for i in list1:
#     new = i+1
#     list2.append(new)
# print(list2)

# list2=[i+1 for i in list1]
# print(list2)

# name="fFtgga"
# list2=[i for i in name]
# print(list2)

# conditional list comprehension
# list1 =['tfzst','etAE','dtSET','sdgz']
# list2=[n for n in list1 if len(n)<5]
# print(list2)

# dictonary comprehension
# import random
# names=["rzsery","rysery","etga","serdghasz","ryhzs"]
#
# student_dic ={i:random.randint(1,100) for i in names}
# print(student_dic)
#
# pass_student = {student:score for (student,score) in student_dic.items() if score > 50}
# print(pass_student)

# dictionary
#
# dict1={
#     "student":["tegt","dtgzse"],
#        "marks":[22,45]
#        }
#
#
# data = pd.DataFrame(dict1)
# print(data)
#
# #loop through dataframe
# for (key,value) in data.items():
#     print(value)
#
# #loop through row
# for (index,row) in data.iterrows():
#     print(index)
#
# for (index,row) in data.iterrows():
#     if row.student == "tegt":
#         print(row.marks)
