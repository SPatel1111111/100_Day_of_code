# # Q.1 : How do you check the type of a variable in Python?
# # Ans : using 'type' keyword we can find the variable type in python.It shows the output in form of "<class 'type'>".
# example
val1 = 5
print(type(val1))

val2 = 'hi'
print(type(val2))

val3 = 5.4
print(type(val3))

# # Q.2 : Write a Python program to reverse a string.
# string = "Python is a popular programming language."

# # Ans :
str2 ="Python is a popular programming Language."

list1=list(str2)
# using slicing in list
list2 =(list1[::-1])

reverse_str =""
for i in list2:
    reverse_str += str(i)

print(reverse_str)

# # Q.3 : How can you check if a string contains only digits?
# string1 = "58465875"
# string2 = "58465O75"
# # Ans :

string1 = "58465875"
if string1.isdigit():
    print("only containing digit")

string2 = "adf35445646"
if string2.isdigit():
    print("only containing digit")
else:
    print("not only digits")

# # Q.4 : How do you replace a "Java" with "Python" in given string ?
# string = "Java is a popular programming language."
# # Ans :

string1 = "Java is a popular programming language."
x = string1.replace("Java", "Python")
print(x)

# # Q.5 : How do you split a given string from ","?
# string = "hello, my name is Peter, I am 26 years old"
# # Ans :
string = "hello, my name is Peter, I am 26 years old"
list1 = []
j = 0
for j in string:
    string1 = ""
    for i in string:
        if i != ',':
            string1 += i
        else:
            j = i + 1
            break
    list1.append(str(string1))

print(list1)

#this is simple version
string = "hello, my name is Peter, I am 26 years old"
list1 = string.split(",")  # Using the built-in split function

# Printing the result
print(list1)
# # Q.6 : Perform this below given operation on a list ?
# list1 = [1, 2, 3, 4, 5, 6]
# list2 = [1, 5, 7, "Jay", "Meet", "Priti", "Maya", 3, 5, "Jay", 8, 1, 5]
# 1. Add 6, 7, 8, 10 in the list
# 2. Remove '6' from list
# 3. Add '9' on 3rd index
# 4. Reverse a list
# 5. Sort a list in ascending order.
# 6. Find the index of 5
# 7. Join two list list1 and list2
# 8. Remove duplicate items from list2
# Ans :
list1 = [1, 2, 3, 4, 5, 6]
list2 = [1, 5, 7, "Jay", "Meet", "Priti", "Maya", 3, 5, "Jay", 8, 1, 5]
#1
list2.append(6)
list2.append(7)
list2.append(8)
list2.append(10)
print(list2)
#2
list2.remove(6)
print(list2)
#3
list2.insert(3, 9)
print(list2)
#4
list2.reverse()
print(list2)
#5
print(list1.sort())
#6
x=list1.index(5)
print(x)
#7
list1.extend(list2)
print(list1)
##8
list2 = [1, 5, 7, "Jay", "Meet", "Priti", "Maya", 3, 5, "Jay", 8, 1, 5]
set1 = set()
for i in list2:
    if i not in set1:
        set1.add(i)
print(set1)
list2=list(set1)
print(list2)

# set1 =set(list2)
# list1 =list(set1)
# print(list1)

# Q.7 : here in tuple given user data: name, age and department.Unpack a tuple into variables.
# tpl = ("Jay", 28, "Python")
# Ans :
tpl = ("Jay", 28, "Python")
a,b,c=tpl
print(a)
print(b)
print(c)

# # Q.8 : Perform this below given operation on a dictionary ?
# dict1 = {}
# dict2 = {}
# 1. Add name=Joy, age=28 and department=HR in dict1 using dict method
# 2. Add city=Anand, state=Guj and country=Ind in dict2
# 3. Add all values of dict2 in dict1 using method (merge two dictionaries)
# 4. Print all keys and values of dict1 after done operation 3
# 5. How can I find the length of a dictionary
# # Ans :
#1
dict1 = dict({
    "name":"joy",
    "age" :28,
   "department":"HR"
    })
print(dict1)

#2
dict2 ={
        "city":"anand",
        "state":"Gujarat",
        "Country":"India"
        }
print(dict2)

#3
dict1.update(dict2)
print(dict1)

#4
print(dict1.keys())
print(dict1.values())

#5
print(len(dict1))


# # Q.9 : Create a function which can gives two input from user and perform given operations sum, multiplication, division, subtraction and return all values.
 # Ans :

def operations(a, b):
    add = a + b
    mul = a * b
    sub = a - b
    if b != 0:
        div = a / b
    else:
        print("b is 0")

    return {"add": add, "mul": mul, "sub": sub, "div": div}


a = int(input("enter any number1:"))
b = int(input("enter any number2:"))
result = operations(a, b)
print(result["add"])
print(result["mul"])
print(result["sub"])
print(result["div"])

# # Q.10 : Create one function that takes number input from user and print upto zero to that number.
# 1. using for loop
# 2. using while loop
# # Ans :

def my_fun(n):
    if n>=0:
        # using for loop
        for i in range(n,-1):
            print(i)
        # using while
        while n >= 0:
            print(n)
            n -= 1
    else:
        # using for loop
        for i in range(n,1):
            print(i)
        # using while
        while n >= 0:
            print(n)
            n += 1

n = int(input("enter any number:"))
result = my_fun(n)