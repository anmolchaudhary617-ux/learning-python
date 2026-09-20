user_name = input("Please enter your full name: ")

def display_name(name):
  first_name = None
  last_name = None
  # a ssuming the first word is name and the last word is the last name and the name doesn't include father's/mother's name
  for i in user_name:
    if(i == " "):
      first_name = user_name[: i]
      last_name = user_name[i+1 :]
  
