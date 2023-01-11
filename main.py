print("Welcome to the tip calculator.")
total_bill = float(input("What was the total bill? $"))
percent = int(input("What percentage tip would you like to give? 10, 12 or 15? "))
people = int(input("How many people to split the bill? "))
new_percent = percent / 100 + 1
split_bill = (total_bill * new_percent) / people

print(f"Each person should pay: ${round(split_bill,2)}")