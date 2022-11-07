#!/usr/bin/python3
# A function that does exactly the same
# as the python btytecode


def magic_calculation(a, b):
    result = 0
    for r in range(1, 3):
        try:
            if r > a:
                raise Exception('Too far')
            else:
                result += a ** b / r
        except:
            result = b + a
            break
    return(result)
