#!/usr/bin/env python3
import sys
def main():
    if len(sys.argv) != 3:
        print("none")
    else:
        a = int(sys.argv[1])
        b = int(sys.argv[2])
        c = list(range(a, b + 1))
        print(c)
main()