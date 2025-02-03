# neg = []
# pos = []
# def myfunc(*args):
#     for i in args:
#         if i < 0:
#             neg.append(i)
#         else:
#             pos.append(i)
#
#
# myfunc(7, 5, -6)
# print(neg)
# print(pos)

#
# def lesser_of_two_evens(a, b):
#     if a % 2 == 0 and b % 2 == 0:
#         return min(a, b)
#     else:
#         return max(a, b)
#
#
# result=lesser_of_two_evens(2, 5)
# print(result)


# def animal_crackers(word):
#     list1 = word.split()
#     return list1[0][0] == list1[1][0]
#
#
# result = animal_crackers("hello hi")
# print(result)

# def make_twenty(a, b):
#     return (a+b)==20 or a==20 or b==20
# 
# result = make_twenty(2, 2)
# print(result)

# def absolute_there(n):
#     return (abs(100 -n) <= 10) or (abs(200 - n) <= 10)
#
#
# r=absolute_there(109)
# print(r)

# def has_33(list1):
#     for i in range(len(list1)-1):
#         if list1[i] == 3 and list1[i + 1] == 3:
#             return True
#     return False
#
#
# r = has_33([2, 34, 4, 3, 3])
# print(r)

# def paper_doll(text):
#     result = ''
#     for char in text:
#         result += char * 3
#     return result
#
# r=paper_doll("hello")
# print(r)

# def blackjack(a, b, c):
#     sum1=int(a + b + c)
#     print(sum1)
#     if sum1 > 21:
#         if a==11 or b==11 or c==11:
#             return sum1 -10
#         else:
#             return "BUST"
#     else:
#         return sum1
#
#
# r = blackjack(9, 10, 11)
# print(r)


