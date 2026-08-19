user_weight = float(input('Weight: '))
weight_unit = input("(L)bs or (K)g: ")
if weight_unit.lower() == "l":
    converted_weight = round(0.453592*user_weight, 1)
    print(f"You are {converted_weight} kilos")
elif weight_unit.lower() == "k":
    converted_weight = round(2.20462*user_weight, 1)
    print(f"You are {converted_weight} pounds")
else: 
    print('Please enter a valid input!')