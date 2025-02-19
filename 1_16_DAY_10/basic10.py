# class
# class my_class:
#     x=11
# obj =my_class()
# print(obj.x)

# init function
# class person:
#     def __init__(self,fn,ln):
#         self.fn = fn
#         self.ln = ln
#
# p1 = person("as","sa")
#
# print(p1.fn)
# print(p1.ln)

# str method for directly show result of the object
# class hey:
#     def __init__(self,name,age):
#         self.name =name
#         self.age = age
#
#     def __str__(self):
#         return f"{self.name} and {self.age}."
#
# h1 = hey("sa",30)
# print(h1)

# object method
# class nope:
#     def __init__(self,name, age):
#         self.name = name
#         self.age = age
#
#     def obj_fun(self):
#         print(f"hello,{self.name}")
#
# n1=nope("dfzsg",20)
# n1.obj_fun()

# self parameter
# self keywored used to refernce the parameter. so instead of using self, we also use somthing else.
# class nice:
#     def __init__(say,name,age):
#         say.name =name
#         say.age =age
#     def __str__(say):
#         return f"hey{say.name}."
#
# x1 = nice("hello",32)
# print(x1)

# modify object property
# class ice:
#     def __init__(self,me):
#         self.me = me
#
# i=ice("ertgw")
# i.me ="hello"
#
# print(i.me)

# delete object property
# class delete:
#     def __init__(self,me):
#         self.me =me
# d =delete("rfgzsg")
# # del d.me
# # del d
# print(d)

# pass keyword
# without pass statement it raised an error when it empty
# class pass_me:
#     pass

# inheritance
# class Base:
#     def __init__(self, fn, ln):
#         self.fn = fn
#         self.ln = ln
#
#     def my_fun(self):
#         print(f"firstname:{self.fn}")
#
# class Child(Base):
#     pass
#
# b1 = Child("my","me")
# b1.my_fun()

# class Parent:
#     def __init__(self,fn,ln):
#         self.fn =fn
#         self.ln=ln
#
#     def my_output(self):
#         print(self.fn,self.ln)
#
# class Child(Parent):
#     def __init__(self,f1,l1):
#         Parent.__init__(self,f1,l1)
#
# c = Child("HELLO","HI!!")
# c.my_output()

# using super function we can access the parents all methods
# class Base:
#     def __init__(self, me):
#         self.me = me
#     def new(self):
#         print(self.me)
# class Top(Base):
#     def __init__(self, me):
#         super().__init__(me)
# x = Top("hi")
# x.new()

# add properties
# class Base:
#     def __init__(self,me):
#         self.me =me
#     def new(self):
#         print(self.me)
# class Top(Base):
#     def __init__(self,me):
#         super().__init__(me)
#         self.year =2025
# x=Top("hello")
# print(x.year)
# OR
# class Top(Base):
#     def __init__(self,me,year):
#         super().__init__(me)
#         self.year1 =year
#
# x=Top("hello",2025)
# print(x.year1)


# ADD METHOD
# class parent:
#     def __init__(self,fn):
#         self.fn=fn
#     def my(self):
#         print(self.fn)
# class child(parent):
#     def __init__(self,fn,me,year):
#         super().__init__(fn)
#         self.year=year
#         self.me=me
#
#     def my1(self):
#         print(f"hey!!{self.fn} and {self.me} at {self.year} .")
#
# x=child("demon","ele",2025)
# x.my1()
# x.my()

# ITERATORS
# list1=[1,2,3,4,5]
# itr1=iter(list1)
#
# print(next(itr1))
# print(next(itr1))
#
# st="banana"
# itr2=iter(st)
# print(next(itr2))
# print(next(itr2))

# class iterable:
#     def __iter__(self):
#         self.a =1
#         return self
#
#     def __next__(self):
#         x=self.a
#         self.a+=1
#         return x
#
# my = iterable()
# it =iter(my)
#
# print(next(it))
# print(next(it))
# print(next(it))

# class iter1:
#     def __iter__(self):
#         self.a=1
#         return self
#     def __next__(self):
#         if self.a <=20:
#             x=self.a
#             self.a+=1
#             return x
#         else:
#             raise StopIteration
# me=iter1()
# y=iter(me)
# for i in y:
#     print(i)

# polymorphism
# class car:
#     def __init__(self,brand,model):
#         self.model=model
#         self.brand=brand
#     def move(self):
#         print("drive!")
# class boat:
#     def __init__(self,brand,model):
#         self.model = model
#         self.brand = brand
#     def move(self):
#         print("sail!")
# class plane:
#     def __init__(self,brand,model):
#         self.brand=brand
#         self.model=model
#     def move(self):
#         print("fly!!")
#
# c= car("fwt","fge")
# b= boat("dfge","efgea")
# p= plane("sfwf","fffg")
#
# for i in (c,b,p):
#     i.move()

#inheritance class polymorphism

class vehical:
    def __init__(self,brand,model):
        self.brand=brand
        self.model=model

    def move(self):
        print("move!")
class car(vehical):
    pass
class boat(vehical):
    def move(self):
        print("sail!!")
class plane(vehical):
    def move(self):
        print("fly!!")

c = car("frr","frre")
b= boat("rfwr","sff")
p =plane("dfa","faefg")

for i in (c,b,p):
    print(i.brand)
    print(i.model)
    i.move()
