# positional only argument
# def my_fun(a,b,/):
#     print(a)
#     print(b)
# my_fun(10,11)

# def my_fun(a,b):
#     print(a,b)
# my_fun(b=11,a=12)

#keyword only argument
# def my_fun(* ,a):
#     print(a)
# my_fun(a=10)

#combine positional only and keyword only
# def my_fun(a,b,/,*,c,d):
#     print(a,b,c,d)
#
# my_fun(1,2,c=11,d=12)

#recursion
#function called it's self
# def recursion_f(a):
#     if a >0:
#         sum1=a+recursion_f(a-1)
#         return sum1
#     else:
#         return 0
#
# print(recursion_f(6))

#lamda function
# a=lambda i:i**2
# print(a(5))

# a= lambda x,y:x*y
# print(a(2,4))

# def my_fun(n):
#     return lambda a :a**n
# obj =my_fun(2)
# print(obj(11))

#array
# arr1 =[1,2,3,4,5]
# arr1[0]=11
# print(arr1)
# arr1.append(33)
# print(arr1)
# arr1.pop(0)
# print(arr1)
# arr1.remove(33)
# print(arr1.index(3))
# print(len(arr1))
#
# for i in arr1:
#     print(i)

#class
# class my_class:
#     x=11
# obj =my_class()
# print(obj.x)

#init function
# class person:
#     def __init__(self,fn,ln):
#         self.fn = fn
#         self.ln = ln
#
# p1 = person("as","sa")
#
# print(p1.fn)
# print(p1.ln)

#str method for directly show result of the object
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

#object method

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

#self parameter
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

#modify object property
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
