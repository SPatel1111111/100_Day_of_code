name = input("enter name:")
email = input("enter mail:")
birth_date = input("enter birth date:")
dict1 = {"Name": name, "Email": email, "Birth": birth_date}
print(dict1)
with open(f"{name}.txt", mode="w") as new:
    for key,value in dict1.items():
        new.write(f"{key}:{value}")
        new.write("\n")
