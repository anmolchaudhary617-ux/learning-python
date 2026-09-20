number_of_terms = int(input("Enter the number of terms you would like to see in python: "))

def fibonacci_seq(n):
  if n <= 0:
    return "The number of terms must be greater than or equal to 1"

  seqeunce = [0, 1]

  if n == 1:
    return [0]
  elif n == 2:
    return seqeunce
  else:
    for i in range(2, n):
      next_term = seqeunce[-1] + seqeunce[-2]
      seqeunce.append(next_term)
      
    return seqeunce


print(fibonacci_seq(number_of_terms))