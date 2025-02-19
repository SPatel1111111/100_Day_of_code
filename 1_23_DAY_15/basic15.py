# import camelcase
#
# c =camelcase.CamelCase()
#
# text ="hello world"
#
# print(c.hump(text))
#

# try catch
# try:
#     print(x)
# except NameError:
#     print("x variable not define")
# except:
#     print("error occur")
#
# try:
#     print(5)
# except:
#     print("error.")
# else:
#     print("there is no error.")

# try:
#     print(x)
# except:
#     print("error....")
# finally:
#     print("finally called")

# try:
#     f=open("my.txt")
#     try:
#         f.write("hello")
#     except:
#         print("it is not going to write down.")
#     finally:
#         f.close()
# except:
#     print("it is not going to open file.")

# raise exception

# x =-1
# if x<0:
#     raise Exception("it raise exception error.")
#
# x="hello"
# if not type(x) is int:
#     raise Exception("it only allow integer.")

# FILE HANDLING

# f= open("my.txt")
# x=f.read()
# print(x)
#
# f=open("my.txt","r")
# x=f.read()
# print(x)

# f=open("my.txt","w")
# f.write("hello")

# f=open("my.txt","a")
# f.write("hello")

# f=open("D:/SNEHA1/100_Day_of_code/23_1_DAY_15/my.txt","r")
# print(f.read())

# f=open('my.txt','r')
# # print(f.read(5))
# #
# # f=open('my.txt',"r")
# # print(f.readline())
# # print(f.readline())
#
# f=open("my.txt","r")
# for x in f:
#     print(x)

# f=open("my.txt","r")
# print(f.readline())
# f.close()
#
# f=open("new.txt","x")

import os
# os.remove("new.txt")
#
# if os.path.exists("new.txt"):
#     os.remove("new.txt")
# else:
#     print("this file doesn't exist.")

# os.rmdir("ex")

# Pandas

import pandas as pd
#
# df = pd.read_csv("username.csv")
# # it gives summarise version of the csv file  when it too large
# print(df)
# # it gives whole file
# print(df.to_string())

# print(pd.options.display.max_rows)

#create dataframe
# data ={
#     "cars":["car1","car2","car3","car4"],
#     "passing":[1,2,3,4]
# }
# print(pd.DataFrame(data))

#pandas version
# print(pd.__version__)

#pandas Series
# s1 =[1,2,3,"zs"]
# y=pd.Series(s1)
# print(y)
# print(y[3])

# s2=[1,3,5,6]
# x=pd.Series(s2,index=["x","y","z","w"])
# print(x)
# print(x["y"])

# calories={"day1":200,"day2":300,"day3":400}
# x=pd.Series(calories)
# y=pd.Series(calories,index=["day1","day2"])
# print(x)
# print(y)


#Dataframe
data ={
    "cars":["car1","car2","car3","car4"],
    "passing":[1,2,3,4]
}
x = pd.DataFrame(data)
print(x)
# print(x.loc[0])
print(x.loc[[0,1,2,3]])

