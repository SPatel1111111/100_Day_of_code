#CONDITIONS
a =11
b =11
if a> b:
    print("yeah,it is correct")
elif a==b:
    print("both are equal.")
else:
    print("nope, it is less than b.")

if a==b : print("yes")

print("a") if a<=b else print("b")

c= 19
d =12
if a<b and c<d:
    print("hey")

if a<b or c<d:
    print("nope")

if not c<b:
    print("yeah")

# nested if
if a==b:
    if a<c:
        print("yes")
    else:
        print("nope")

# pass statement
if b>a:
    pass
