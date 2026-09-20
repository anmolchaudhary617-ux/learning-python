def find_longest_word(word_list):
    if not word_list:
        return "The list is empty."
    
    longest_word = word_list[0]
    
    for word in word_list:
        if len(word) > len(longest_word):
            longest_word = word
            
    return longest_word

words = ["Python", "Programming", "List", "Data", "ComputerScience"]

result = find_longest_word(words)

print("Input List:", words)
print("The longest word is:", result)