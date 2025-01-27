# import tkinter
#
# window = tkinter.Tk()
# window.title("FIRST TKINTER")
# window.minsize(500,300)
#
# tk_lable =tkinter.Label(text="hello world",font=("arial"))
# tk_lable.pack()
#
# window.mainloop()


# arbitrary argument

# def add(*args):
#     sum = 0
#     for i in args:
#         sum += i
#     return sum
#
#
# print(add(1, 2, 3, 4, 5, 6, 7))
#
#
# # arbitrary keyword argument
# def ke(n, **kwargs):
#     print(kwargs)
#     # for (i,j) in kwargs.items():
#     #     print(i)
#     #     print(j)
#     n += kwargs["add"]
#     n *= kwargs["multiply"]
#     print(n)
#
# ke(2, add=3, multiply=5)
#
# class Car:
#     def __init__(self,**kwargs):
#         self.make=kwargs["make"]
#         self.model=kwargs["model"]
#
# myobj =Car(make="my-make",model="new")
# print(myobj.model)
#
# class Car:
#     def __init__(self,**kwargs):
#         self.make=kwargs.get("make")
#         self.model=kwargs.get("model")
#
# myobj =Car(make="my-make")
# print(myobj.model)


# pending learn
import pandas as pd

list1 =["ntgwet","feth@gmail.com","rysery12344"]
list2 =["name","email","password"]

data = pd.DataFrame(list1)
print(data)

# data1=pd.Series(list1,index=["name","email","password"])
# print(data1)
# data=pd.DataFrame(data1)
# print(data)

dict2=data.to_dict()
print(dict2)

dict3 = {i:row for (index,row) in data.iterrows() for i in list2}
print(dict3)