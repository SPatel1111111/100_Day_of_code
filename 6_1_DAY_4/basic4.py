# data structure
#list
list1 =[1,2,3,4,1]
# print(list1)
# print(len(list1))

list2=[1,"hi",True,]
# print(list2)
# print(type(list2))

list3 =list((1,2,3,5))
# print(list3)
# print(list3[1])
# print(list3[-2])
# print(list3[2:5])
# print(list3[-1:-3])
#
# if "hi" in list2:
#     print("yes it is.")

# list3[0]=0
# print(list3)
#
# list3[2:4]=[2,3,4]
# print(list3)
#
# list3.insert(0,11)
# list3.append(99)
# list3.extend(list2)
# list3.remove(2)
# list3.pop(0)
# del list3[3]
# print(list3)
#
# list1.clear()
#
# for i in list3:
#     print(i)
#
# for i in range(len(list3)):
#     print(list3[i])
#
# i=0
# while i < len(list3):
#     print(list3[i])
#     i = i+1

# listn=[i for i in list3 if i<5]
# print(listn)
#
# listnn2=["hello" for x in list3 ]
# print(listnn2)
#
# new =[i if i !=1 else 4  for i in list3]
# print(new)
#
# list3.sort()
# list3.sort(reverse=True)
#
# tlist = ["banana", "Orange", "Kiwi", "cherry"]
#
# tlist.sort(key = str.lower)
# print(tlist)
#
# list3.reverse()
#
# new_1 =list3.copy()
# print(new_1)
# new_2=new_1[:]
#
# #join
# print(list1 +list2)
#
# for i in list3:
#     list2.append(i)
#
# list2.extend(list1)
#
# print(list1.count(1))
#
# print(list1.index(2))

# TUPLE
# tuple1 =(1,2,3,4)
# print(tuple1)
# len(tuple1)
# type(tuple1)
# t2=tuple((1,2,3,4,5,6,7))
#
# print(t2[1])
# print(t2[::-1])
# # for modification
# l1=list(t2)
# print(l1)
# l1[0]=111
# l1.append(9)
# l1.remove(3)
# t2=tuple(l1)
# print(t2)
# # tuple to tuple add
# x =(7,)
# t2 += x
# print(t2)
# #del tuple1
#
# # unpack tuple
# t3 =("hi","bye")
# (x,y )=t3
# print(x)
#
# #astrisk
# (x,y,*e)=t2
# print(e)

# for i in t3:
#     print(i)
#
# for i in range(len(t3)):
#     print(t3[i])
#
# i=0
# while i < len(t3):
#     print(t3[i])
#     i=i+1
# # join
# t4 = t3 + t2
# print(t4)
#
# t5 = t3 * 2
# print(t5)
#
# print(t3.count("hi"))
# print(t3.index("hi"))

# set
# s1 ={1,2,3,4,5,6,1,3}
# print(s1)
#
# print(len(s1))
# print(type(s1))
#
# s2 =set((1,2,3,89,7,6))
# print(s2)

# for i in s2:
#     print(i)
#
# print( 89 in s2)
#
# print( 89 not in s2)
#
# s2.add(33)
#
# # merge with any type of data in set
# s2.update(s1)
# # if element not present in the set it raise error
# s2.remove(89)
# # it doesn't raise any error
# print(s2.discard(0))
#
# s2.pop()
# # del s2
# #s2.clear()
#
# for i in s2:
#     print(i)

# join sets
# s3=s1.union(s2)
# s33=s1 | s2
# s333= s1.union(s2,s33)
# s3333 =s1.update(s2)
#
# s4=s1.intersection(s2)
# s1.intersection_update(s2)
# s44 = s1 & s2
#
# s5=s1.difference(s2)
# s1.difference_update(s2)
# s55 =s1 - s2
#
# s6=s1.symmetric_difference(s2)
# s66 = s1 ^ s2
# s1.symmetric_difference_update(s2)

# DICTIONARY
# d1 = {"n":1,"x":2,"y":3}
# print(d1["n"])
# print(len(d1))
# print(type(d1))
#
# d2 =dict({"hi":1,"ice":2})
# print(d2.get("hi"))
#
# d2["bye"]=3
#
# d2.keys()
# d2.values()
#
#
# d2["ice"]=44
# print(d2.items())
#
# if "ice" in d2:
#     print("yeah this is present in the d2 ")
#
# d1.update({"n1":121})
# print(d1)
#
# d1.pop("x")
# d1.popitem()
# print(d1)
#
# del d1["n"]
#
# print(d1)

# for x in d2:
#     print(x)
#
# for i in d2.values():
#     print(i)
# for i in d2.keys():
#     print(i)
# for i in d2.items():
#     print(i)
#
# d3 = d2.copy()
# print(d3)
# #nested loop
# d4 = { "child1":d1 ,"child2":d2, "child3":d3}
# print(d4)
#
# print(d4["child1"]["y"])
#
# for i ,j in d4.items():
#     print(i)
#     for k in j:
#         print(k+":",j[k])

