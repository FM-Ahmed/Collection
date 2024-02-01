class convert_number_system:
    def __init__(self):
        pass
    
    def bin_to_dec(self, binary_string):   
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

    def dec_to_bin(self, decimal_number):
        '''
        Convert a decimal number to binary number

        Args:
        - dec_integer (int): decimal number

        Returns:
        - str: binary representation of decimal number
        '''
        if not isinstance(decimal_number, int):
            raise ValueError(f'Input must be an integer.') # check if the input is valid

        binary_digits = []
        while decimal_number > 0:
            mod = decimal_number % 2
            binary_digits.append(mod)
            decimal_number //= 2

        binary_number = ''.join(map(str, binary_digits[::-1]))
        return binary_number

    def dec_to_hex(self, decimal_number):
        '''
        Convert a decimal number to hex number

        Args:
        - decimal_number (integer): decimal number

        Returns:
        - (str): hex equivalent of decimal input
        '''
        hex_values = {0: '0',
                      1: '1',
                      2 : '2',
                      3: '3',
                      4: '4',
                      5: '5',
                      6: '6',
                      7: '7',
                      8: '8',
                      9: '9',
                      10: 'A',
                      11: 'B',
                      12: 'C',
                      13: 'D',
                      14: 'E',
                      15: 'F'}

        ans = []
        floor = float('inf')
        while floor != 0:
            div = decimal_number / 16
            floor = decimal_number // 16
            remainder = div - floor
            ans.append(hex_values[int(remainder*16)])
            decimal_number = floor
        return ''.join(ans[::-1])
