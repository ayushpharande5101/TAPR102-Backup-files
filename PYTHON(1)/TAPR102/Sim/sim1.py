A = 16122
B = 17142

A1 = str(A)
A2 = str(B)

C = A2 + A1
D = int(C)
print(bin(A))
print(bin(B))

binary_code = bin(D)[2:].zfill(32)

print(binary_code)