"""
The price of a house is $1M($1,000,000). 
If a buyer has a good credit, they have to pay 10% as DP(Down Payment) and 
if they have a bad credit, they need to pay 20% as DP. Print the DP that a buyer has to pay
"""
print('The price of the house is $1M($1,000,000).')
approval = input('To continue, type okay: ')
if approval.lower() == "okay": 
   credit = int(input('Enter your credit: '))  
   if credit >= 800:
       print("You have to pay 10% DP of $1M i.e., $100,000")
   else: 
      print("You have to pay 20% DP of $1M i.e., $200,000")
 
else: 
    print('Thank you for visiting!')




