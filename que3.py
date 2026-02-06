# User will input (2numbers).Write a program to swap the numbers

num1 = int(input("Enter num1: "))
num2 = int(input("Enter num2: "))

temp = num1
num1 = num2
num2 = temp

print(f"num1 = {num1}, num2 = {num2}")