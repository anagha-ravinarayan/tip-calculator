# Tip Calculator
print("Welcome to the tip calculator!")
total = float(input("What was the total bill? $"))
tip = int(input("How much tip would you like to give? 10, 12, or 15? "))
people = int(input("How many people to split the bill? "))

total_tip = total * (tip / 100)
total_amount = total + total_tip
amount_per_person = round(total_amount / people, 2)

print(f"Each person should pay: ${amount_per_person}")