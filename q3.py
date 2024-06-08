def s_box1(input_6bit):
   
    S1 = [
        [14, 4, 13, 1, 2, 15, 11, 8, 3, 10, 6, 12, 5, 9, 0, 7],
        [0, 15, 7, 4, 14, 2, 13, 1, 10, 6, 12, 11, 9, 5, 3, 8],
        [4, 1, 14, 8, 13, 6, 2, 11, 15, 12, 9, 7, 3, 10, 5, 0],
        [15, 12, 8, 2, 4, 9, 1, 7, 5, 11, 3, 14, 10, 0, 6, 13]
    ]
    

    assert len(input_6bit) == 6 and all(bit in '01' for bit in input_6bit), "Input must be a 6-bit binary string."
    

    row = int(input_6bit[0] + input_6bit[5], 2)  # Convert bits to decimal
    col = int(input_6bit[1:5], 2)  # Convert bits to decimal
    
 
    s_box_value = S1[row][col]
    
    output_4bit = f'{s_box_value:04b}'
    
    return output_4bit

# Example usage:
input_6bit = '011011'  # Example 6-bit input
output_4bit = s_box1(input_6bit)
print(f"Input: {input_6bit} -> Output: {output_4bit}")
