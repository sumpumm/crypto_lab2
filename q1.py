def permute(block, table):
    return [block[i - 1] for i in table]

def initial_permutation(block):
    ip_table = [
        58, 50, 42, 34, 26, 18, 10, 2,
        60, 52, 44, 36, 28, 20, 12, 4,
        62, 54, 46, 38, 30, 22, 14, 6,
        64, 56, 48, 40, 32, 24, 16, 8,
        57, 49, 41, 33, 25, 17, 9, 1,
        59, 51, 43, 35, 27, 19, 11, 3,
        61, 53, 45, 37, 29, 21, 13, 5,
        63, 55, 47, 39, 31, 23, 15, 7
    ]
    return permute(block, ip_table)

def final_permutation(block):
    fp_table = [
        40, 8, 48, 16, 56, 24, 64, 32,
        39, 7, 47, 15, 55, 23, 63, 31,
        38, 6, 46, 14, 54, 22, 62, 30,
        37, 5, 45, 13, 53, 21, 61, 29,
        36, 4, 44, 12, 52, 20, 60, 28,
        35, 3, 43, 11, 51, 19, 59, 27,
        34, 2, 42, 10, 50, 18, 58, 26,
        33, 1, 41, 9, 49, 17, 57, 25
    ]
    return permute(block, fp_table)

def binary_string_to_list(binary_string):
    return [int(bit) for bit in binary_string]

def list_to_binary_string(bit_list):
    return ''.join(str(bit) for bit in bit_list)

# Example usage
if __name__ == "__main__":
    # Example 64-bit block
    input_block = '0000000100100011010001010110011110001001101010111100110111101111'  # Example 64-bit binary string

    # Convert the binary string to a list of integers
    bit_list = binary_string_to_list(input_block)
    
    # Apply initial permutation
    permuted_block = initial_permutation(bit_list)
    print("After Initial Permutation: ", list_to_binary_string(permuted_block))

    # Apply final permutation
    final_permuted_block = final_permutation(permuted_block)
    print("After Final Permutation: ", list_to_binary_string(final_permuted_block))