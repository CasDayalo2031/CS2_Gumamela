import math

# Asks the user to enter the coordinates of the first point
x1 = float(input("Enter x1: "))
y1 = float(input("Enter y1: "))
# Asks the user to enter the coordinates of the second point
x2 = float(input("Enter x2: "))
y2 = float(input("Enter y2: "))

# Computing the distance using the distance formula
A = pow(x2 - x1, 2)
B = pow(y2 - y1, 2)
answer = A + B
distance = math.sqrt(answer)

# Displays the result to the user
print ("The distance is: ", distance, "(❁´◡`❁)")
