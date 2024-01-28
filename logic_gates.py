class logic_gates:
    def __init__(self):
        pass
    
    def validate_binary(self, binary_inputs):
        if not isinstance(binary_inputs, str) or (not all(bit in '01' for bit in binary_inputs)):
            raise ValueError(f'Input must be a n-bit binary number.') # check if the input is valid
    
    def not_gate(self, binary_inputs):
        self.validate_binary(binary_inputs)
        if len(binary_inputs) == 1:
            return '1' if int(binary_inputs) == 0 else '0'
        else:
            raise ValueError(f'String cannot {len(binary_inputs)} characters. Must be 1 character long.')
        
    def and_gate(self, binary_inputs):
        self.validate_binary(binary_inputs)
        return '0' if not all(i in '1' for i in binary_inputs) else '1'
    
    def nand_gate(self, binary_inputs):
        self.validate_binary(binary_inputs)
        return '1' if not all(i in '1' for i in binary_inputs) else '0'
        
    def or_gate(self, binary_inputs):
        self.validate_binary(binary_inputs)
        return '1' if any (i in '1' for i in binary_inputs) else '0'
    
    def xor_gate(self, binary_inputs):
        self.validate_binary(binary_inputs)
        return '1' if sum([int(i) for i in binary_inputs]) in range(1, len(binary_inputs) + 1, 2) else '0'
    
    def nor_gate(self, binary_inputs):
        self.validate_binary(binary_inputs)
        return '1' if sum([int(i) for i in binary_inputs]) == 0 else '0'
    
    def xnor_gate(self, binary_inputs):
        self.validate_binary(binary_inputs)
        return '1' if sum([int(i) for i in binary_inputs]) in (0, len(binary_inputs)) else '0'
