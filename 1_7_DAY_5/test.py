# def my_operation(a,b):
#     add =a+b
#     sub =a-b
#     mul = a*b
#     if b >0:
#         div =a/b
#     else:
#         print("b is 0.")
#
#     return add,sub ,mul,div
#
#
# result1,result2,result3,result4= my_operation(6,2)
# print(result1)
# print(result2)
# print(result3)
# print(result4)


def my_sqauare(n):
     return n **2

#map
list1 = [1,2,3,4,5,6,7,8,9,10]
for i in map(my_sqauare, list1):
     print(i)

#list
print(list(map(my_sqauare, list1)))

#filter it only filter based on function that it true than return value
print(list(filter(my_sqauare, list1)))

# with help pf lamda
print(list(map(lambda n : n ** 2 ,list1)))
print(list(filter(lambda n : n % 2 ==0, list1)))
#
# var = lambda a: a + 1
# print(var(10))



























