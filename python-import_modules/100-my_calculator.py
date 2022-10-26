#!/usr/bin/python3
from sys import argv
from calculator_1 import add, sub, mul, div

if __name__ == "__main__":
    args = len(argv)

    if args != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
                                
        a = int(argv[1])
        e= argv[2]
        b = int(argv[3])

    if e == "+":
        num = add(a, b)
    elif e == "-":
        num = sub(a, b)
    elif e == "*":
        num = mul(a, b)
    elif e == "/":
        num = div(a, b)
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
    print("{:d} {} {:d} = {:d}".format(a, e, b, num))
