#day2 
# tip calculator
# asks for the total, percentage tip (10, 12, 15), and how many will split the bill
# the calculator will determine how much each person will have to pay

print("Welcome to the tip calculator!")

#input the total bill
total_bill = float(input("What is the total bill? "))

#input tip percentage and conversion
tip_percentage = int(input("How much tip would you like to give? 10, 12, or 15? "))
tip_percentage = float(1+(tip_percentage/100))

#total bill with percentage
total_bill = total_bill * tip_percentage

#input how many people to split the bill
people_to_split = int(input("How many people to split the bill? "))

bill_per_person = round((total_bill/people_to_split),2)

#output
print(f"Each peroson should pay: ${bill_per_person}")



