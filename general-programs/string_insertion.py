s1 = input("Enter string 1: ")
s2 = input("Enter string 2: ")
position = int(input("Enter position: "))

print(f"After inserting \"{s2}\" at \"{position}\" index of \"{s1}\", we get \"{s1[ : position] + s2 + s1[position : ]}\"") 