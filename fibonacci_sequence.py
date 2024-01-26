def fibonacci_sequence(n):
    '''
    Generates Fibonaccu numbers to the n-th term
    Input
    n (int): how many numbers of the fibonacci sequence you are interested in.
    Output
    fibonacci (list): length of returned list is n+1 because the sequence starts with index 0.
    '''
    if n < 1:
        return []
    
    fibonacci = [0, 1]
    for i in range(1, n):
        new_val = fibonacci[i] + fibonacci[i-1]
        fibonacci.append(new_val)   
    return fibonacci
