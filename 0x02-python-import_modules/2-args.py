#!/usr/bin/python3
import sys

if __name__ == "__main__":
    argv = sys.argv

    if len(argv) == 1:
        print("0 arguments.")
    elif len(argv) == 2:
        print("{} argument:".format(len(argv) - 1))
        for arg in range(1, len(argv)):
            print("{}: {}".format(arg, argv[arg]))
    else:
        print("{} arguments:".format(len(argv) - 1))
        for arg in range(1, len(argv)):
            print("{}: {}".format(arg, argv[arg]))
