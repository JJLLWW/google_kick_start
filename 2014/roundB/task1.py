#!/usr/bin/python3

# password attacker

# know keys but not ntimes pressed or in what order

# M keys pressed, password is N chars. 1 <= M

# each possible password is an N arrangement over a set S of M elements where each
# element of S is used at least once. (inclusion-exclusion?)

# total = M**N

# count number of possible passwords mod 10**9 + 7

# (!) math.comb is new in Python 3.8 so can't use it here (!)

import math
# import sys

def comb(n, k):
    return math.factorial(n)//(math.factorial(k)*math.factorial(n-k))

# count with inclusion-exclusion
def solve(M, N):
    total_arr = M**N
    key_missing_arr = 0
    for i in range(1, M):
        key_missing_arr += (-1)**(i-1)*comb(M, M-i)*(M-i)**N
    n_pass = total_arr - key_missing_arr
    n_pass_mod = n_pass % (10**9 + 7)
    return n_pass_mod

def main():
    ncases = int(input())
    for case in range(1, ncases+1):
        words = input().split()
        M, N = int(words[0]), int(words[1])
        npassmod = solve(M, N)
        print(f"Case #{case}: {npassmod}")

# print(sys.version)
main()