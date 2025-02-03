# calculator

def add(num1,num2):
    return num1 + num2

def mul(num1,num2):
    return num1 * num2

def div(num1,num2):
    if num2 != 0:
        return num1 / num2

def sub(num1,num2):
    return num1 - num2

operation = {'+': add, '-': sub, '*': mul, '/': div}
print(" hey,Do you want to perform operation like  addition ,subtraction, multiplication and division ???")

def calculator():
    n1 = float(input("enter first number:"))
    should = True
    while should:
        for sym in operation:
            print(sym)
        symbol =input("enter the operation symbol you want perform:")

        n2= float(input("enter second number:"))

        result = operation[symbol](n1,n2)
        print(f"{n1} {symbol} {n2} = {result}")

        choice = input(f"enter 'y' if you want contiune with calculation result {result} and 'n' if you want do new calculation and 'e' for end:").lower()
        if choice == 'y':
            n1 = result
        elif choice =='n':
            should = False
            calculator()
        else:
            end=print("Exit")
            return end

calculator()

