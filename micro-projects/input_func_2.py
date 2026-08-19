"""
Write a program that does the following:
Ask the user to enter their full name
Convert the name so that:
The first letter of each word is capital
Print:
The formatted name
The number of characters in the name (excluding spaces)
"""
user_name = input('Please enter your full name: ')
full_name = user_name.title()
full_name_without_space = full_name.replace(" ", "")
print(full_name)
print(len(full_name_without_space))