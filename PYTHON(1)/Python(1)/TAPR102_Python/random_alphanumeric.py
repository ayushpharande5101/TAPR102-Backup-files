import numpy as np
import string
import secrets
def alphanumeric_random(num):
    num = 10

    res = ''.join(secrets.choice(string.ascii_letters + string.digits) for x in range(num))

    return str(res)

print(alphanumeric_random(10))