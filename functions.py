import numpy as np

# Function check_prime uses the following definition of prime numbers:
# It is a prime IF it can be divided by EXACTLY two numbers.
# I.e. 1 is not a prime.

def check_prime(n):
        # Input:
            # n: some arbitrary whole number.
        # Output:
            # is_prime: returns either True or False.
        
    if type(n) != int:
        raise ValueError('Input {} is not a whole number... Please provide an integer.'.format(n))
        
    nums = np.arange(1,n+1,1)
    frac_list = []
    
    for value in nums:
        if value <= n:
            frac = float(n/value)
            frac_list.append(frac)
    
    count = 0
    for number in frac_list:
        if str(number).endswith('.0'):
            count += 1
            if count >= 3:
                break
    if count == 2:
        is_prime = True
    else:
        is_prime = False  
        
    return is_prime

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
