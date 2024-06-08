# Expansion P-box table
EXPANSION_P_BOX = [
    32, 1, 2, 3, 4, 5,
    4, 5, 6, 7, 8, 9,
    8, 9, 10, 11, 12, 13,
    12, 13, 14, 15, 16, 17,
    16, 17, 18, 19, 20, 21,
    20, 21, 22, 23, 24, 25,
    24, 25, 26, 27, 28, 29,
    28, 29, 30, 31, 32, 1
]


def expand(input_bits):

    if len(input_bits) != 32:
        raise ValueError("Input must be a 32-bit binary string")
    
    output_bits = []

    
    for position in EXPANSION_P_BOX:
    
        output_bits.append(input_bits[position - 1])


    return ''.join(output_bits)


input_block = '11001100110011001100110011001100'  # Example 32-bit input
expanded_block = expand(input_block)
print(f"Input Block (32-bit) : {input_block}")
print(f"Expanded Block (48-bit): {expanded_block}")
