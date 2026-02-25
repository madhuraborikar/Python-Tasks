# Write a program to find the simple interest when the value of principle,rate of interest and time period is given


principle = int(input("Enter the principle: "))
rate_of_interest = float(input("Enter the rate of interest: "))
time_period = float(input("Enter the time period(in years): "))

simple_interest = (principle *  rate_of_interest * time_period)/100

print(f"The Simple Interest is: {simple_interest}")