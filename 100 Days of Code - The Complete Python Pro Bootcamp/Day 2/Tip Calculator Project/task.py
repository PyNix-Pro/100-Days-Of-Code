print("Welcome to the tip calculator!")
Bill = float(input("What was the total bill? $ "))
Tip = int(input("How much tip would you like to give? 10, 12 or 15? "))
People = int(input("How many people to split the bill? "))
Final_Payment_By_Each_Person = round(((Tip/100 + 1) * Bill) / People, 2)
print(f"Each person should pay: ${Final_Payment_By_Each_Person}")


