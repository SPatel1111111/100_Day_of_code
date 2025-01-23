name = input("enter name:")
email = input("enter mail:")
birth_date = input("enter birth date:")

list2 = ["Name:", "Email:", "Birth:"]
list1 = [name, email, birth_date]


print(list1)
with open(f"{name}.txt", mode="w") as new:
    for j in range(len(list2)):
        new.write(list2[j])
        new.write(list1[j])
        new.write("\n")



