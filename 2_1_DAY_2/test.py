import random
import string

letters = []

s1 = string.ascii_letters

for char in s1:
    letters.append(char)

numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

symbols = ['@', '#', '$', '%', '*', '!']

l = int(input("letters you want:"))
n = int(input("number you want:"))
s = int(input("symbols you want:"))

pass1 = ""

for i in range(0, l):
    pass1 += random.choice(letters)

for i in range(0, n):
    pass1 += str(random.choice(numbers))

for i in range(0, s):
    pass1 += random.choice(symbols)

print(pass1)

