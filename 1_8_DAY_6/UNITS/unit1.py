# #1
# print("Hello World")

#2 Create a program to find whether given number is odd or even. [Take input from user]
#
# n =int(input("enter number:"))
# if n % 2 ==0:
#     print("n is even number.")
# else:
#     print("odd")

# # 3 Take input from user and find factorial of a number.
# def fact(n):
#     var = 1
#     if n > 0:
#         for i in range(1, n + 1):
#             var = var * i
#
#     return var
#
#
# n = int(input("enter number:"))
# r = fact(n)
# print(r)

# # 4 Using while loop print Fibonacci series.
# def fibonacci(n):
#     a = 0
#     b = 1
#     count =0
#     list1 = []
#     if n == 1:
#         list1.append(n)
#     if n > 1:
#         list1.append(a)
#         list1.append(b)
#         while count < n-2:
#             c = a + b
#             list1.append(c)
#             a, b = b, c
#             count +=1
#     return list1
#
#
# r = fibonacci(10)
# print(r)

#5 Print the following pattern
# A
# A B
# A B C
# A B C D
# A B C D E
n = int(input("enter rows:"))
for i in range(n):
    ascii_val = 65
    for j in range(i+1):
        a = chr(ascii_val)
        print(a, end =" ")
        ascii_val +=1
    print()



































