
# User will input (3ages).Find the oldest one


age1 = int(input("Enter First age: "))
age2 = int(input("Enter second age: "))
age3 = int(input("Enter second age: "))

if age1>age2 and age1>age3:
    print(f"{age1} is larger than {age2} and {age3}")
elif age2>age3 and age2>age1:
    print(f"{age2} is larger than {age3} and {age1}")
else:
    print(f"{age3} is larger than {age1} and {age2}")