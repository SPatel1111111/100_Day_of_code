# #normally open file
# with open("weather_data.csv") as data:
#     d=data.read()
#     print(d)

# with csv
import csv
from typing import List, Any

# with open("weather_data.csv") as data:
#     d=csv.reader(data)
#     for i in d:
#         print(i)

# with open("weather_data.csv") as data:
#     d = csv.reader(data)
#     temperature =[]
#     for i in d:
#         if i[1] != "temp":
#             temperature.append(int(i[1]))
#
#     print(temperature)

# with pandas
import pandas as pd
df=pd.read_csv("weather_data.csv")
print(type(df))
print(type(df["temp"]))
print(df)
# print(df["temp"])


