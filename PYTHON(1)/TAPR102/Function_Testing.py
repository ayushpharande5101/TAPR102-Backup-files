# def split_ascii_value(value):
#     high_byte = value >> 8
#     low_byte = value & 0xFF
#     return high_byte, low_byte
# #-------------------------------------------------------------------------------------------------------------------------------
# def for_list(a):
#     result = ""
#     for i in a:
#         value = i
#         high_byte, low_byte = split_ascii_value(value)
#
#         if (65 <= low_byte <= 90 or 48 <= low_byte <= 57 or low_byte == 32) and low_byte != 0:
#             result += chr(low_byte)
#             #return chr(low_byte)
#
#         if (65 <= high_byte <= 90 or 48 <= high_byte <= 57 or high_byte == 32) and high_byte != 0:
#             result += chr(high_byte)
#             #return chr(high_byte)
#     return result
#
# a = [83 ,84, 65, 84 ,73 ,79 ,78, 32, 65]
# print(for_list(a))
#***************************************************************************************************************************

import struct

def concatenate(list1):
    if list1[0] < 0:
        a = bin(list1[0])[3:]
        b = bin(list1[1])[2:]
    elif list1[1] < 0:
        a = bin(list1[0])[2:]
        b = bin(list1[1])[3:]
    else:
        a = bin(list1[0])[2:]
        b = bin(list1[1])[2:]

    if list1[0] < 0:
        a = bin(list1[0])[3:]
        b = bin(list1[1])[2:]
    elif list1[1] < 0:
        a = bin(list1[0])[2:]
        b = bin(list1[1])[3:]
    else:
        a = bin(list1[0])[2:]
        b = bin(list1[1])[2:]

    print(list1)
    print(a)
    print(b)

    binary_code = a.zfill(16)
    binary_code1 = b.zfill(16)
    concatenated_binary = binary_code1 + binary_code
    return concatenated_binary
#---------------------------------------------------------------------------------------------------------------------
def binary_to_float_ieee754(binary_string):
    # Convert the binary string to a 32-bit unsigned integer
    ieee754_bits = int(binary_string, 2)

    # Pack the integer into binary data
    packed_data = struct.pack('!I', ieee754_bits)

    # Unpack the binary data as a float number
    float_number = struct.unpack('!f', packed_data)[0]

    return float_number

# Example usage
list_of_numbers = [-1704, 17045]

concatenated_binary = concatenate(list_of_numbers)
resulting_float = binary_to_float_ieee754(concatenated_binary)

print("Concatenated Binary:", concatenated_binary)
print("Resulting Float:", resulting_float)

number = 123.456789
decimal_part = str(number).split('.')[1]
A = int(decimal_part) * 2
B = str(int(number)) + "." + str(A)
print(B)

print(type(B))  # This will be a string

# If you want to convert B to an integer, you can do the following:
B_as_integer = int(float(B))
print(B_as_integer)
print(type(B_as_integer))  # This will be an integer


# 00111110111110100100001011110110
# 01000010111101100011111011111010

# +ve number = 01000010111101100011111011111010
# -ve number = 00111110111110100100001011110110  (2nd digit)
# -ve number = 01000010111101100011111011111010  (1st digit)

"""
[17142, -16122]
100001011110110
11111011111010

[16122, -17142]
11111011111010
100001011110110

00111110111110100100001011110110
"""