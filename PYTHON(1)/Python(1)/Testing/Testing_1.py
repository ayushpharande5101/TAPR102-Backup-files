def split_ascii_value(value):

  high_byte = value >> 8
  low_byte = value & 0xFF
  return high_byte, low_byte

k = [23, 45, 56, 78]
for i in k:
    value = i
    high_byte, low_byte = split_ascii_value(value)
    #print(high_byte)  # 123
    #print(low_byte)  # 45

    if ((65 <= low_byte <= 90) or (48 <= low_byte <= 57)) and low_byte != 0:
        print(chr(low_byte), end="")

    if ((65 <= high_byte <= 90) or (48 <= high_byte <= 57)) and high_byte != 0:
        print(chr(high_byte), end="")

split_ascii_value(value)
