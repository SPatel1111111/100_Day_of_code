# # 6 Create a program to find whether given number is palindrome or not.
# def palindrome(n):
#     if n>0:
#         new=str(n)
#         return new == new[::-1]
#     else:
#         str1 =" enter positive number."
#         return str1
#
# n = int(input("enter number:"))
# r=palindrome(n)
# print(r)

# #7 Create a list in python and perform following operations:
# # a) Print length of the list
# # b) Append an item to the list
# # c) Insert an item to the list
# # d) Find index number of an item
# # e) Remove an item from list
# # f) Delete an item with specified index
#
# list1=[1,2,3,5]
# print(len(list1))
# list1.append(10)
# list1.insert(2,4)
# print(list1.index(4))
# list1.remove(4)
# list1.pop(0)
#print(list1)

# #8
# # Given a tuple
# # n= (19, 147, 36, 87, 97, 239, 6, 34)
# # a) Display elements of tuple
# # b) Display lowest tuple elements
# # c) Display largest tuple elements
# # d) Difference between largest and lowest tuple element
# n= (19, 147, 36, 87, 97, 239, 6, 34)
# #a
# print(n)
# #b
# n1=list(n)
# n1.sort()
# low=n1[0]
# print(low)
# #c
# high=n1[-1]
# print(high)
# #d
# diff =high -low
# print(diff)

# #9
# # Return a new set of identical items from two sets in Python.
# # e.g.
# # set1 = {10, 20, 30, 40, 50}
# # set2 = {30, 40, 50, 60, 70}
# # O/p:
# # {40, 50, 30}
#
# set1 = {10, 20, 30, 40, 50}
# set2 = {30, 40, 50, 60, 70}
# print(set1.intersection(set2))
#
#10 pattern
# n=5
# for i in range(1,n+1):
#     for k in range(n-i):
#         print(" ",end="")
#     for j in range(i):
#         print("*",end="")
#     print()

# pyramid
n=5
for i in range(1,n+1):
    for k in range(n-i):
        print(" ",end="")
    for j in range(2*i-1):
        print("*",end="")
    print()

# # 11
# # Write a Python program to generate and print a dictionary that contains a number
# # (between 1 and n) in the form (x, x*x).
# # e.g.
# # Input: 10
#
# def dict_square(n):
#     dict1 = {}
#     for i in range(n+1):
#         dict1[i]=i*i
#     return dict1
#
# r = dict_square(10)
# print(r)









