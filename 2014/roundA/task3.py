#!/usr/bin/python3

# Cut Tiles:

# want N square tiles with side lengths 2**S1, 2**S2, ..., 2**SN
# needs to make them by cutting up MxM square tiles (can only cut parallel to the
# sides)

# we must have 2**Si <= M, so there is ALWAYS a solution.

def solve(N, M, S):
    return 69

def main():
    ncases = int(input())
    for case in range(1, ncases+1):
        words = input().split()
        N, M = int(words[0]), int(words[1])
        S = [int(Si) for Si in words[2:]]
        S.sort(reverse=True)
        nbuy = solve(N, M, S)
        print(f"Case #{case}: {nbuy}")

if __name__ == "__main__":
    main()