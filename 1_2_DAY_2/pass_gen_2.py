# random password generator
import random
import string

letters=list(string.ascii_letters)
numbers = [0,1,2,3,4,5,6,7,8,9]
symbols = ['@','#','$','&','*','*','!','(',')']

print(" the letters, symbol , num  you want are:")
total_le = int(input("enter the letter you want:"))
total_sy = int(input("enter the total symbol you want:"))
total_num = int(input("enter total number you want:"))

pass_list = []

for i in range(1,total_le + 1):
    pass_list.append(random.choice(letters))

for i in range(1 ,total_sy + 1):
    pass_list.append(random.choice(letters))

for i in range(1,total_num+1):
    pass_list.append(random.choice(letters))

print(pass_list)

pass1 = []
pass1.append(random.shuffle(pass_list))
print(pass1)

password1 =""
for char in pass1:
    password1 += pass1[i]

print(password1)