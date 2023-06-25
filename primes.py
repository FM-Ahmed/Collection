import numpy as np

def primes(n):
        # Input:
            # n: some arbitrary whole number.
        # Output:
            # prime_numbers: a list of prime numbers between 1 and n.
        
    if type(n) != int:
        raise ValueError('Input {} is not a whole number... Please provide an integer.'.format(n))
        
    nums = np.arange(1,n+1,1)
    
    prime_numbers = []
    for value in nums:
        result = check_prime(int(value))
        if result == True:
            prime_numbers.append(value) 
            
    return prime_numbers
