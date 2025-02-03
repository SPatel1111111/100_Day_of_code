#
# class Animal:
#     def __init__(self):
#         self.num_of_eyes = 2
#
#     def breath(self):
#         print("Inhale,Exhale")
#
# class Fish(Animal):
#     def __init__(self):
#         super().__init__()
#
#     def breath(self):
#         super().breath()
#         print("doing this under water")
#     def swim(self):
#         print("moving in water.")
#
#
# f = Fish()
# f.swim()
# f.breath()
# print(f.num_of_eyes)

#file management
# file = open("my_file.txt")
# content =file.read()
# print(content)
# file.close()
#
with open("my_file.txt") as f:
    content =f.read()
    print(content)

# with open("my_file.txt",mode="w") as f:
#     f.write("new text.")

# with open("my_file.txt",mode="a") as f:
#     f.write("\nnew text.")

with open("new_file.txt",mode="w") as f:
    f.write("new file.")

