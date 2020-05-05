print("Calculation of Area and Circumference of a Circle")

import math

radious = float (input("Please enter the Radious of the Circle :  "))

area = math.pi * (radious ** 2)
circumference = 2 * math.pi * radious

print("The Area of the Circle is :  ", round(area,2))
print("The Circumference of the Circle is :  ", round(circumference,2))
