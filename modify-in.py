import argparse
import sys

import pylatexenc.latex2text



def modify_in(input_str):
    pass



def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("input")
    parser.add_argument("output")
    args = parser.parse_args()

    if args.input == "-":
        input_str = sys.stdin.read()
    else:
        with open(args.input, "r") as f:
            input_str = f.read()
    output_str = modify_in(input_str)
    if args.output == "-":
        sys.stdout.write(output_str)
    else:
        with open(args.output, "w") as f:
            f.write(output_str)


if __name__ == "__main__":
    main()
