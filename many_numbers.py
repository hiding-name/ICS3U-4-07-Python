#!/usr/bin/env python3

# Created by: Matsuru Hoshi
# Created on: Sept 2019
# This is program prints all numbers form 1000 to 2000 in 5 numbers per line


def main():
    # variable
    keep_upper = 0

    # process & output
    for number in range(1000, 2001):
        print(number, sep="", end=" ")
        if keep_upper % 5 == 4:
            print("")
        keep_upper = keep_upper + 1


if __name__ == "__main__":
    main()
