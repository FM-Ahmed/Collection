def bin_to_dec(binary_string):   
    '''
    Convert a binary number to decimal number
    
    Args:
    - binary_string (str): binary number in string format
    
    Returns:
    - int: decimal equivalent of binary input 
    '''
    bits = len(binary_string) # determine number of bits
    if not all(bit in '01' for bit in binary_string):
        raise ValueError(f'Input must be a n-bit binary number.') # check if the input is valid
    
    # convert to binary and return in decimal form
    vals = []
    for i in range(0, len(binary_string)):
        vals.append(int(binary_string[i]) * 2**((bits-1)-i))
    return sum(vals)
