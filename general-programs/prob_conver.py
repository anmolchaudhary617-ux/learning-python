"""
Write a program to ask the user's weight(in pounds).
Convert into kg and print it. 
"""
user_weight = input('What is your weight?: (In pounds)')
user_weight_in_kg = round(0.45359237*float(user_weight), 3)
print('Your weight is', user_weight, 'in lb(pounds) and', user_weight_in_kg, 'in kg(kilograms)')   