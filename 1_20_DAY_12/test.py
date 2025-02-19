def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def multiplication(a,b):
    return a*b
def calculation(a,b,func):
    return func(a,b)

r1=calculation(10,20,multiplication)
print(r1)