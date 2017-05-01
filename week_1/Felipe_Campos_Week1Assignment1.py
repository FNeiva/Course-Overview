# Python Bridge Week 1 Assignment 1
# Felipe Campos

n_gallons = input("Number of gallons of gasoline:")
n_liters = float(n_gallons) * 3.7854
n_barrels = float(n_gallons) / 19.5
price = float(n_gallons) * 3.65

print(str(n_gallons) + " gallons of gasoline: ")
print("- Are equivalent to " + str(n_liters) + " liters of gasoline")
print("- Require " + str(n_barrels) + " barrels of oil to produce")
print("- Cost on average $" + str(price))
