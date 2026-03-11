#!/usr/bin/env python3

"""
Script to compute the smallest prime factor of a given positive integer.

Usage:
    python script.py <integer>

Example:
    python script.py 15
    Output: 3
"""

import sys


def smallest_prime_factor(n):
    """Return the smallest prime factor of n."""
    for i in range(2, n):
        if n % i == 0:
            return i
    return n


def main():
    """Parse arguments and run the program."""
    
    if len(sys.argv) != 2:
        sys.exit(f"{sys.argv[0]}: Expecting one command line argument -- the integer to factor")

    try:
        n = int(sys.argv[1])
    except ValueError:
        sys.exit("Error: Argument must be an integer")

    if n < 1:
        sys.exit(f"{sys.argv[0]}: Expecting a positive integer")

    result = smallest_prime_factor(n)
    print(result)


if __name__ == "__main__":
    main()
