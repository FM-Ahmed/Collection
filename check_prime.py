def check_prime(x):
    '''
        Input:
            x (int): some arbitrary whole number.
        Returns:
            bool: True if prime, False if not
    '''
    if not isinstance(x, int) or x < 1:
        raise ValueError(f'Input {x} is invalid. Please provide a positive integer above 1.')
        
    if (x % 2 == 0 and x != 2) or x == 1:
        return False
        
    rng = range(3, int(np.sqrt(x) + 1), 2)
    for num in rng:
        if x % num == 0: 
            return False
    return True
