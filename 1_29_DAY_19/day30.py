# is_ok=messagebox.askokcancel(title="website",message=f"These are details entered: \n Email:{email} \nPassword :{password} \nIs it ok to save?")
# if is_ok:
#     with open("data.txt","a") as data_file:
#         data_file.write(f"{web} | {email} | {password}\n")
#         website_Entry.delete(0,END)
#         pass_entry.delete(0,END)

#udemy day30
# file error
# with open("new-file.txt") as file:
#     file.read()

# index error
# list1=[1,4,5,7]
# print(list1[4])

# # key error
# dict1 ={"key1":"value1"}
# val=dict1["not_exit_key"]
# print(val)

# type error
# str ="hello"
# print(str + 5)

# try:
#     file = open("new_file.txt")
#     dict1 = {"key1": "value1"}
#     print(dict1["key1etety"])
#
# except FileNotFoundError:
#     print("hi")
#     file = open('new_file.txt',"w")
#     file.write("hello")
# except KeyError as message_error:
#     print(f"here key error {message_error}")
# else:
#     content = file.read()
#     print(content)
# finally:
#     file.close()
#     print("file closed.")
    # raise TypeError("this error ...")

#bmi calculator
# weight =int(input("enter weight:"))
# height =int(input("enter height:"))
# if height > 3:
#     raise ValueError
# bmi = weight / height ** 2
#
# print(bmi)



