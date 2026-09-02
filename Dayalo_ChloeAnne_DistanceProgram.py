import math

x1 = float(input("Enter x1: "))
y1 = float(input("Enter y1: "))
x2 = float(input("Enter x2: "))
y2 = float(input("Enter y2: "))

A = pow(x2 - x1, 2)
B = pow(y2 - y1, 2)

answer = A + B
distance = math.sqrt(answer)

print ("The distance is: ", distance, "(❁´◡`❁)")
