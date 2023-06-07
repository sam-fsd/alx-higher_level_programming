#!/usr/bin/python3
def islower(c):
    try:
        for l in range(97, 123):
            if ord(c) == l:
                return True;
    except:
        return False
    return False
