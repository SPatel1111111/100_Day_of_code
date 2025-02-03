#importing turtle class to print through object
# from turtle import Turtle,Screen
#
# timmy = Turtle()
# print(timmy)
# timmy.shape("turtle")
# timmy.color("coral")
# timmy.forward(100)
#
# scr =Screen()
# print(scr.canvheight)
# scr.exitonclick()

# from prettytable import PrettyTable
# table = PrettyTable()
# table.add_column("alphabet no.",[1,2,3])
# table.add_column("alphabet",["A","B","C"])
# table.align ='r'
#
# print(table)

#DAY_17
# class New:
#     def __init__(self,id,name):
#         self.id=id
#         self.name=name
#         self.followers=0
#
# user1=New("001","gss")
# user2=New("002","sdgs")
# print(user1.id)
# print(user1.followers)
# print(user2.followers)
#
# class User:
#     def __init__(self,id,name):
#         self.id =id
#         self.name=name
#         self.follower=0
#         self.following=0
#
#     def follow(self,user):
#         user.follower +=1
#         self.following +=1
#
# user1=User("001","gss")
# user2=User("002","sdgs")
# user3=User("003","ggszg")
#
# user1.follow(user2)
# user3.follow(user1)
# user3.follow(user2)
# print(user1.follower)
# print(user1.following)
# print(user2.follower)
# print(user2.following)

# class my:
#     x=10
#
# p1 =my()
# print(p1.x)

#test
class Me:
    def __init__(self,id):
        self.id=id
    def my_fun(self):
        print(self.id)

obj1 =Me("001")
obj1.my_fun()