# def palindrome(s):
#     s = s.replace(' ', '')
#     return s == s[::-1]
#
#
# r = palindrome("nurses run")
# print(r)


# cube = lambda x: x ** 3
# def fibonacci(n):
#     a = 0
#     b = 1
#     list1 = []
#     if n == 1:
#         list1.append(a)
#     if n > 1:
#         list1.append(a)
#         list1.append(b)
#         for _ in range(n - 2):
#             c = a + b
#             list1.append(c)
#
#             a, b = b, c
#     return list1
#
#     # return a list of fibonacci numbers
#
#
# if __name__ == '__main__':
#     n = int(input())
#     print(list(map(cube, fibonacci(n))))