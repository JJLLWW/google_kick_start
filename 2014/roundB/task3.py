#!/usr/bin/python3

# card game

# N cards with positive int number a_i in a list left [index 1] to right [index N].
# positive integer K

# 3 adjacent cards chosen with left to right nums a, b, c
# must have c - b = b - a = K to discard.
# if multiple triples satisfy have to make INTELLIGENT choice which to remove to minimise
# number remaining.

# 

# 1 <= N <= 100

def read_intlist():
    words = input().split()
    lst = [int(word) for word in words]
    return lst

def solve(N, K, A):
    return 0

def main():
    ncases = int(input())
    for case in range(1, ncases+1):
        N, K = read_intlist()
        A = read_intlist()
        y = solve(N, K, A)
        print(f"Case #{case}: {y}")

main()