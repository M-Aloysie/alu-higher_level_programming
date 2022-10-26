#!/usr/bin/python3
from sys import argv
from calculator_1 import add, sub, mul, div

if __name__ == "__main__":
    args = len(argv)

    if args != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
                                
    x = int(argv[1])
    e= argv[2]
    y = int(argv[3])

    if e == "+":
        num = add(x, y)
    elif e  == "-":
        num = sub(x, y)
    elif e == "*":
        num = mul(x, y)
    elif e == "/":
        num = div(x, y)
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
    print("{:d} {} {:d} = {:d}".format(x, e, y, num))
