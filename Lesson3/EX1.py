x = 0
y= 1
try:
    y=2
    print(z)
    1/x
    print("after")
except ZeroDivisionError:
    print("divide by zero")
except NameError:
    z = input("insert z : ")
    print(z)
finally:
    print("done")