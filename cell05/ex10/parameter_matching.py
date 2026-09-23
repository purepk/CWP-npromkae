#!/usr/bin/env python3
import sys
if len(sys.argv) != 2:
    print("none")
else:
    a = sys.argv[1]
    b = input("What was the parameter? ")
    if b == a:
        print("Good job!")
    else:
        print("Nope, sorry...")