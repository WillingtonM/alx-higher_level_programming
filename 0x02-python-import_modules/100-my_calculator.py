#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    import sys

    operators = ["+", "-", "*", "/"]
    argv_count = len(sys.argv[1:])

    if argv_count != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)
    elif sys.argv[2] not in operators:
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)
    else:
        a = int(sys.argv[1])
        b = int(sys.argv[3])
        operator = sys.argv[2]
        if sys.argv[2] == "+":
            result = add(a, b)
        elif sys.argv[2] == "-":
            result = sub(a, b)
        elif sys.argv[2] == "*":
            result = mul(a, b)
        elif sys.argv[2] == "/":
            result = div(a, b)

        print("{:d} {:s} {:d} = {:d}".format(a, operator, b, result))
