def split_ascii_value(value):
    high_byte = value >> 8
    low_byte = value & 0xFF
    return high_byte, low_byte
#-------------------------------------------------------------------------------------------------------------------------------
def for_list(a):
    result = ""
    for i in a:
        value = i
        high_byte, low_byte = split_ascii_value(value)

        if (65 <= low_byte <= 90 or 48 <= low_byte <= 57) and low_byte != 0:
            result += chr(low_byte)
            #return chr(low_byte)

        if (65 <= high_byte <= 90 or 48 <= high_byte <= 57) and high_byte != 0:
            result += chr(high_byte)
            #return chr(high_byte)
    return result
#--------------------------------------------------------------------------------------------------------------------
def concatenate(list1):
    if list1[0] < list1[1]:
        list1[0], list1[1] = list1[1], list1[0]
        if list1[0] < 0:
            a = bin(list1[0])[3:]
            b = bin(list1[1])[2:]
        elif list1[1] < 0:
            a = bin(list1[0])[2:]
            b = bin(list1[1])[3:]
        else:
            a = bin(list1[0])[2:]
            b = bin(list1[1])[2:]

    else:
        if list1[0] < 0:
            a = bin(list1[0])[3:]
            b = bin(list1[1])[2:]
        elif list1[1] < 0:
            a = bin(list1[0])[2:]
            b = bin(list1[1])[3:]
        else:
            a = bin(list1[0])[2:]
            b = bin(list1[1])[2:]
        pass

    concatenated_binary = '0' + a + '0' + b
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

#-----------------------------------------------------------------------------------------------------------------------
