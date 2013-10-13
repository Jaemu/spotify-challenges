#!/usr/bin/python
import sys

def reverse(origin):
        origin = bin(origin)[::-1]
        newint = int(origin[:-2],2)
        print newint

def main():
    for line in sys.stdin:
        reverse(int(line))

if __name__=="__main__":
    main()