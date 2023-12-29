def concatenate(list1):
    a = str(list1[0])
    b = str(list1[1])

    result = a + b
    return int(result)

def floating_Point_Represnation(list2):
    result = concatenate(list2)
    conversion = bin(result)

    return conversion

l = [89,98]
print(floating_Point_Represnation(l))