import struct

def decimal_to_binary(number):
    if number == 0:
        return '0b0'
    binary = ''
    while number > 0:
        remainder = number % 2
        binary = str(remainder) + binary
        number = number // 2
    return  binary

# Example usage:

def concatenate(list1):
    a = bin(list1[0])[2:]
    b = bin(list1[1])[2:]

    concatenated_binary = '0' + b + '0'+ a
    return concatenated_binary

my_list = [17793, 17323]
result = concatenate(my_list)
print(result)

def binary_to_float_ieee754(binary_string):
    # Convert the binary string to a 32-bit unsigned integer
    ieee754_bits = int(binary_string, 2)

    # Pack the integer into binary data
    packed_data = struct.pack('!I', ieee754_bits)

    # Unpack the binary data as a float number
    float_number = struct.unpack('!f', packed_data)[0]

    return float_number

#01000101100000010100001110101011
# Example usage:
binary_representation =  result #'100001110101011100010110000001'
float_number = binary_to_float_ieee754(binary_representation)
print(float_number)
