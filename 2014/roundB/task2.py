#!/usr/bin/python3

# New Years Eve

# triangular pyramid of glasses, each horizontal plane a level.
# Levels numbered from 1 (highest) to 2, 3, 4, ...
# In each level glasses numbered from 1 to L*(L+1)/2

# each glass holds 250ml, when full overflows equally into the 3 glasses below it.

# B bottles 750ml each poured (into the top glass?)

# need num ml y in glass L, N.


# what are the indeces of the 3 glasses below a glass with index i?

ml_in_bot = 750
ml_in_glass = 250

def solve(B, L, N):
    n_ml = B*ml_in_bot
    return 0

def main():
    ncases = int(input())
    for case in range(1, ncases+1):
        words = input().split()
        [B, L, N] = [int(word) for word in words]
        y = solve(B, L, N)
        print(f"Case #{case}: {y}")

main()