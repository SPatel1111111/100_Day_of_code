import random

'''
heads_or_tails = random.randint(0,1)

if heads_or_tails == 0 :
    print("heads")
else:
    print("tails")
'''

# who will pay bill

friends =['f1','f2','f3','f4','f5']
print(random.choice(friends))

index1 = random.randint(0,5)
print(f"{friends[index1]} will pay bill.")

