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
    """
    Expands a 32-bit input block to a 48-bit output block using the DES Expansion P-box.
    
    :param input_bits: A string of 32 bits (e.g., '101010...').
    :return: A string of 48 bits after expansion.
    """
    if len(input_bits) != 32:
        raise ValueError("Input must be a 32-bit binary string")
    
    # Initialize the output bits list
    output_bits = []

    # Use the expansion P-box to expand the input_bits
    for position in EXPANSION_P_BOX:
        # Append the bit from the input_bits at the specified position (1-indexed)
        output_bits.append(input_bits[position - 1])

    # Join the list into a single string and return
    return ''.join(output_bits)

# Example usage
input_block = '11001100110011001100110011001100'  # Example 32-bit input
expanded_block = expand(input_block)
print(f"Input Block (32-bit) : {input_block}")
print(f"Expanded Block (48-bit): {expanded_block}")
