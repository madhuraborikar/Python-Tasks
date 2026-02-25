# Write a program to find the volume of the cylinder. Also find the cost when ,when the cost of 1litre milk is 40Rs

import math

pi=3.14

radius = float(input("Enter the radius: "))
height = float(input("Enter the height: "))

volume = pi*radius**2*height

print(f"The volume is: {volume}")

cost_of_milk = volume*40
print(f"The cost of milk is: {cost_of_milk}")


# math.pi*r**2*h