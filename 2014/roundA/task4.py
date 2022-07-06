#!/usr/bin/python3

# Addition:

# (variable names can be strings)
# B gets equations in form x+y=Z where x,y variable names and Z is some integer.
# you get given N equations with correct answers.
# then Q equations with no answers x+y=?

def main():
    ncases = int(input())
    for case in range(1, ncases+1):
        N = int(input())
        for _ in range(N):
            vars = input().split(sep='+')
        Q = int(input())
        for _ in range(Q):
            pass

main()