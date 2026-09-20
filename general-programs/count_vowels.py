"""
This programs takes a string and returns the number of vowels in it.
"""
s = input("Enter a string: ")

vowel_counter = 0

for ch in s:
  if(ch in "aeiouAEIOU"):
    vowel_counter += 1

print(f"{s} has {vowel_counter} vowels in it.")