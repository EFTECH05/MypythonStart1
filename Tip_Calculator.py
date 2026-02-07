  # Ask the user for inputs
print("welcome to turkish Doner house ")
bill = float(input("What is the total bill? "))
tip_percent = float(input("How much tip would you like to give? (10, 12, or 15): "))
people = int(input("How many people to split the bill? "))

# Calculations
tip = bill * (tip_percent / 100)
total_bill = bill + tip
per_person = total_bill / people

# Output
print(f"Each person should pay: {per_person:.2f}")