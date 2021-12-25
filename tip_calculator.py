#code for tip calculator
print("Welcome to the tip calculator!")
bill=input("What was the total bill? ")
bill=float(bill)
tip=input("How much tip would you like to give? 10, 12, or 15? ")
tip=int(tip)
people=input("How many people to split the bill? ")
people=int(people)
total_bill=(bill+(bill*tip*0.01))/people
total_bill="{:.2f}".format(round(total_bill,2))
print(f"Each person will pay {total_bill}")
