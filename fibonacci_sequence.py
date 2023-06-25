def fibonacci_sequence(n):
  # Input
    # n: integer, how many numbers of the fibonacci sequence you are interested in.
  # Output
    # fibonacci: a list with length (n+1). This is because the sequence starts with index 0.
  
    fibonacci = [0, 1]
    for i in range(1, n):
        new_val = fibonacci[i] + fibonacci[i-1]
        fibonacci.append(new_val)   
    return fibonacci
