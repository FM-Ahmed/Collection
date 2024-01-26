def primes(n):
    '''
    Input:
        n (int): some arbitrary whole number.
    Returns:
        prime_numbers (list): a list of prime numbers between 1 and n (including n).
    '''
    if not isinstance(n, int):
        raise ValueError(f'Input {n} is invalid... Please provide an integer.')
        
    nums = range(2, n+1)
    
    prime_numbers = []
    for value in nums:
        if check_prime(int(value)):
            prime_numbers.append(value)            
    return prime_numbers
