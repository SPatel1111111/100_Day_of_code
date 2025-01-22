# # 12
# # Write a Python function that accepts a string and count the number of upper,
# # lower case letters, digits and other characters.
# # Input : How Are You, sir?
# # Output :
# # No. of Upper case characters : 3
# # No. of Lower case Characters : 9
# # No. of Digits : 0
# # No. of Other Characters : 9
# def check(s):
#     upper = 0
#     lower = 0
#     digit = 0
#     other = 0
#     for i in s:
#         if i.isupper():
#             upper += 1
#         elif i.islower():
#             lower += 1
#         elif i.isdigit():
#             digit += 1
#         else:
#             other += 1
#     return upper, lower, digit, other
#
#
# r1, r2, r3, r4 = check("How Are You, sir?")
# print(f"No. of Upper case characters :{r1}")
# print(f"No. of lower case characters :{r2}")
# print(f"No. of Digits :{r3}")
# print(f"No. of Other Characters :{r4}")
# #13
# # Write a Python function that accepts a string and returns the string in Uppercase.
# # Input: Good Morning, sir.
# # Output: GOOD MORNING, SIR.
#
# def upper_case(s):
#     return s.upper()
# r = upper_case("Good Morning, sir.")
# print(r)

# # 14
# # Create a python function that accepts a list of integer elements as an argument and returns a list with ONLY even numbers of elements.
# # Input List : [10, 21, 34, 53, 85, 70, 69]
# # Output List : [10, 34, 70]
#
# def list_fun(list1):
#     list2=[]
#     for i in list1:
#         if i % 2 ==0:
#             list2.append(i)
#
#     return list2
#
# r =list_fun([10, 21, 34, 53, 85, 70, 69])
# print(r)

# #15
# # Write a Python function that takes a list and returns a new list with unique/distinct elements from the first list.
# # Input List : [1, 2, 3, 3, 3, 3, 4, 4, 4, 5]
# # Output List : [1, 2, 3, 4, 5]
#
# def distinct_li(list1):
#     set1=set(list1)
#     list2=list(set1)
#     return list2
#
# r =distinct_li([1, 2, 3, 3, 3, 3, 4, 4, 4, 5])
# print(r)

# # 16
# # Write a python function that accepts a list of string elements as an argument and
# # returns a list with reverse of each element.
# # Input List : [“Anand”, “Borsad”, “Dakor”, “Nadiad”]
# # Output List : [“dnanA”, “dasroB”, “rokaD”, “daidaN”]

# def reverse_l(list1):
#     list2 =[]
#     for i in list1:
#         str(i)
#         str1=i[::-1]
#         list2.append(str1)
#     return list2
#
# r =reverse_l(["Anand", "Borsad","Dakor", "Nadiad"])
# print(r)

# #19
# #Write a python function that accepts a list of string elements as an argument and returns a list with ONLY first letter of each element.
# # Input List : [“Anand”, “Borsad”, “Dakor”, “Nadiad”]
# # Output List : [“A”, “B”, “D”, “N”]
#
# def first_l(list1):
#     list2 =[]
#     for i in list1:
#         str(i)
#         str1=i[0]
#         list2.append(str1)
#     return list2
#
# r =first_l(["Anand", "Borsad","Dakor", "Nadiad"])
# print(r)

# #20
# #Write a python function that accepts a list of string elements as an argument and  returns a list with length of each element.
# # Input List : [“Anand”, “VVN”, “Dakor”, “Nadiad”]
# # Output List : [5, 3, 5, 6]
# def count_str(list1):
#     list2 =[]
#     for i in list1:
#         str(i)
#         len1=len(i)
#         list2.append(len1)
#     return list2
#
# r =count_str(["Anand", "VVN","Dakor", "Nadiad"])
# print(r)

# #21
# #Write a Python function that accepts a list of integer elements as an argument and returns two separate lists of odd and even elements.
# # Original list of integers: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# # Odd numbers list: [1, 3, 5, 7, 9] Even numbers list: [2, 4, 6, 8, 10]
#
# def all_int(list1):
#     odd =[]
#     even=[]
#     for i in list1:
#         if i % 2 == 0:
#             even.append(i)
#         else:
#             odd.append(i)
#
#     return odd,even
#
# od1 ,ev1 =all_int([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
# print(f"Odd numbers list:{od1}")
# print(f"Even numbers list:{ev1}")









