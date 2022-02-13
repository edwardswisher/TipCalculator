#TipCalculator
bill = input("Welcome to the Tip Calculator!\nEnter your bill:")
tipPercent = input("Enter percent you want to tip:")

tipPercentFloat = float(tipPercent) 
billfloat = float(bill)
tipAmount = billfloat * (tipPercentFloat * 0.01)
totalAmount = billfloat + tipAmount

print("Your tip should be:", + tipAmount)
print("Total bill with tip is:", + totalAmount)

