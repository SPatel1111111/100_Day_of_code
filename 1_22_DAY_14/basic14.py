#w3school
#1
# import test
# test.my("you...")
# #2
# x=test.person["age"]
# print(x)

#3
# import test as t
# t.my("edgze")

#4
#bulid in module

# import platform as p
# y=p.system()
# x=p.platform()
# print(x)
# print(y)
#
# z=dir(p)
# print(z)

#5
#only import which are needed
#
# from test import person
#
# print(person["doing"])

#6
# import datetime
# x=datetime.datetime.now()
# print(x)
# print(x.year)
# print(x.strftime("%A"))
# print(x.strftime("%a"))
# #
# # y=datetime.datetime(2025,2,11)
# # print(y)
# print(x.strftime("%B"))
# print(x.strftime("%b"))
# print(x.strftime("%C"))
# print(x.strftime("%c"))
# print(x.strftime("%H"))
# print(x.strftime("%I"))

#7
# # math function
# print(min(1,34,56))
# print(max(45,67,89))
# print(abs(-2.75))
# print(pow(2,2))
#
# import math
#
# print(math.sqrt(64))
# print(math.ceil(2.3))
# print(math.floor(2.3))
# print(math.pi)

#8
#json
# it is used for storing and exchanging data.
# it is written javascript object notation that's it text called JSON text.

#json to python
# import json
# x = '{ "name":"iogha","age":23,"doing":"athletes"}'
# #parse x
# y = json.loads(x)
# print(y)
# print(y["age"])
#
# #python to json
#
# z = json.dumps(y)
# print(z)
#
#
# import json
#
# x ={
#     "name":"dfgse",
#     "age":34,
#     "Married": True,
#     "Divorced": False,
#     "pets":None,
#     "cars":[
#         { "name":"car1","model":"model1"},
#         { "name":"car2","model":"model2"}
#     ]
# }
# r2=json.dumps(x)
# r1 =json.dumps(x,indent=4)
# r0 =json.dumps(x,indent=4,separators=(".","="))
# r3 =json.dumps(x,indent=4,sort_keys=True)
# print(r1)
# print(r2)
# print(r0)
# print(r3)
#
