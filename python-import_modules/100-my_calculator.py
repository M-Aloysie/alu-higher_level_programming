#!/usr/bin/python3
from sys import argv
from calculator_1 import add, sub, mul, div

if __name__ == "__main__":
    args = len(argv)

    if args != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
                                
        x = int(argv[1])
        ab = argv[2]
        y = int(argv[3])

    if ab == "+":
        num = add(x, y)
    elif ab == "-":
        num = sub(x, y)
    elif ab == "*":
        num = mul(x, y)
    elif ab == "/":
        num = div(x, y)
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
    print("{:d} {} {:d} = {:d}".format(x, ab, y, num))
