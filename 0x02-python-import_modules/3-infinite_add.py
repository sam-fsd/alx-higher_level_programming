#!/usr/bin/python3
import sys

if __name__ == "__main__":
    argv = sys.argv
    total = 0

    if argv == 1:
        print("0")

    for arg in range(1, len(argv)):
            total += int(argv[arg])
    
    print("{}".format(total))
