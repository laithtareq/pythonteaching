import random as ra
import math
mark = 0
x,y = ra.randint(1,100),ra.randrange(0,90)
z = x+ra.randrange(0,10)
F = input("insert the correction factor F")
F = float(F)
A1 = input("what is the value of A1 if x = {}, y = {}-degree, z = {} ?".format(x,y,z))
A1 = float(A1)
A1_real = x*math.sin(math.radians(30))
if (A1_real - F <= A1) and  (A1_real + F >= A1):   # A1 between A1_real + F and A1_real - F 
    mark +=5
A2 = input("what is the value of A2 ?")
A2 = float(A2)
A2_real = z - A1*(x+math.cos(math.radians(y)))
if (A2_real - F <= A2) and  (A2_real + F >= A2):
    mark +=5
print("your mark is {} of 10".format(mark))



