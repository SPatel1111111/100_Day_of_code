# # Date : 10-01-2025


# Q.1 : Write a Python program to count the number of vowels in a given string.
# string = "Python is a popular programming language. It was created by Guido van Rossum, and released in 1991."
#
# vowels = [ "a","e","i","o","u"]
# x=0
# for i in string:
#     if i in vowels:
#         x +=1
#     else:
#         continue
# print(x)
# done


# Q.2 : Write a Python code to check if a string is a palindrome.
# "radar" => True
# "hello" => False
# def palindrome(n):
#     if n != "":
#         new=str(n)
#         return new == new[::-1]
#     else:
#         str1 =" enter valid"
#         return str1

# n =input("enter :")

# r= palindrome(n)
# print(r)
# done

# Q.3 : What is a KeyError in Python Dict, and how can you handle it?
# dict_val = {"name": "Jay", "marks" 22"}  # Print location from dict_val
# dict_val = {"name": "Jay", "marks":22 }
# # there is error in the dic_val is : and extra " this
# print(dict_val.get("location"))
# done

# Q.4 : How can you replace string space with a given character in Python?
text = "D t C mpBl ckFrid yS le"
ch = "a"
# new=text.replace(" ",ch)
# print(new)
#done

# Q.5 : Given a positive integer num, write a function that returns True if num is a perfect square else False.
# 10 => False
# 36 => True
# def p(n):
#     x = 1
#     while x * x < n:
#         x += 1
#     return x * x == n
#
# print(p(10))
# print(p(36))
#done
# Q.6 : Write a Python code to convert a list of temperatures from Celsius to Fahrenheit.
# [ Formula : c/5 = f-32/9 [ where c = temperature in celsius and f = temperature in fahrenheit ]
# celsius_values = [20, 10, 22, 17, 16, 5, 1, 23]
# fahrenheit=[]
# for i in celsius_values:
#     F =int(i/5) + (32/9)
#     fahrenheit.append(F)
#
# print(fahrenheit)
#done

# Q.7 : Write a Python code to implement a simple calculator.
# def add(n1,n2):
#     return n1+n2
# def mul(n1,n2):
#     return n1*n2
#
# def div(n1,n2):
#     if n2 != 0:
#         return n1 / n2
# def sub(n1,n2):
#     return n1-n2
#
# d1 = { "+":"add" ,"*":"mul","-":"sub" ,"/":"div"}
#
# num1=int(input("num1:"))
# for i in d1:
#     print(i)
#
# op1=input("operator:")
# num2 =int(input("num2:"))
#
# r = d1[op1](num1,num2)
# print(r)
# done

# Q.8 : Write a Python program that iterates the integers from 1 to 50. For multiples of three print "Fizz" instead of the number and for multiples of five print "Buzz". For numbers that are multiples of three and five, print "FizzBuzz".
#
# def fizbuz(n):
#     for i in range(n+1):
#         if i % 3 == 0 and i % 5 == 0:
#             print("FizzBuzz")
#         elif i % 3 == 0:
#             print("Fizz")
#         elif i % 5 == 0:
#             print("Buzz")
#         else:
#             print(i)
#
# fizbuz(50)
# done

# Q.9 : Write a Python program to create password. Must match below conditions.
# At least 1 letter between [a-z] and 1 letter between [A-Z].
# At least 1 number between [0-9].
# At least 1 character from [$#@].
# Minimum length 6 characters.
# Maximum length 16 characters.
# import random
# import string
#
# numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# cap = string.ascii_uppercase
# low = string.ascii_lowercase
# symbol = ["@", "$", "*", "^"]
#
# def random_pass():
#     password = [
#         random.choice(low),
#         random.choice(cap),
#         random.choice(numbers),
#         random.choice(symbol)
#     ]
#
#     all_char = low + cap + string.digits + ''.join(symbol)
#     password += random.choices(all_char, k=random.randint(2, 12))
#
#     random.shuffle(password)
#     password_str = ''
#     for char in password:
#         password_str += str(char)
#
#     return password_str
#
# password1 = random_pass()
# print(password1)

# Q.10 : Write a Python program to create the multiplication table (from 1 to 10) of a number.
# Expected Output:
# Input a number: 6
# 6 x 1 = 6
# 6 x 2 = 12
# 6 x 3 = 18
# 6 x 4 = 24
# 6 x 5 = 30
# 6 x 6 = 36
# 6 x 7 = 42
# 6 x 8 = 48
# 6 x 9 = 54
# 6 x 10 = 60
#
# n = int(input(" enter:"))
# for j in range(1,11):
#     ans = n * j
#     print(f"{n} * {j} ={ans}")
# done

# Q.11 : Write a program that prints a right-angled triangle pattern of numbers. The size of the triangle should be determined by user input.
# Input: 4
# Output:
# 1
# 12
# 123
# 1234
# n = int(input("enter:"))
#
# for i in range(n+1):
#     for j in range(1,i+1):
#         print(j,end=' ')
#     print()

# done

# Q.12 : Write a function sum_of_digits that takes an integer as input and returns the sum of its digits.
# Input: 1234
# Output: 10
# n = int(input("enter:"))
# sum = 0
# for i in str(n):
#     sum += int(i)
#
# print(sum)
# done

# Q.13 : Write a program to count the frequency of each character in a given string using a dictionary.
# Input: "apple"
# Output: {'a': 1, 'p': 2, 'l': 1, 'e': 1}
# def count_char(in1):
#     char2= {}
#     for char in in1:
#         if char in char2:
#             char2[char] += 1
#         else:
#             char2[char] = 1
#     return char2
#
# in1 = "apple"
# result = count_char(in1)
# print(result)
#done


# Q.14 : Check that given word in text or not.
# str_text = "The art of cooking is both a science and an expression of creativity. It involves combining ingredients in precise proportions while experimenting with flavors and textures to create something unique and delicious."
# word = "Flavors"
#
# if word.upper() in str_text.upper():
#     print("yes")
# else:
#     print("not")
#done

# Q.15 : Write a program that return list of element from 0 to input value using while loop.
# Input : 5
# Output : [1, 2, 3, 4, 5]
# n=int(input("enter:"))
# list2 =[]
# i=0
# while i <= n:
#     list2.append(i)
#     i= i+1
#
# print(list2)
# done
