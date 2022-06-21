#!/usr/bin/python3

# Cut Tiles:

# want N square tiles with side lengths 2**S1, 2**S2, ..., 2**SN
# needs to make them by cutting up MxM square tiles (can only cut parallel to the
# sides)

# we must have 2**Si <= M, so there is ALWAYS a solution.

# Naive Strategy: fill with largest squares first, then try and fill remaining area with
# the largest possible kind of square, etc...

import collections as col
import math

# return how many size s squares can be put inside a rw*rh rectangle. 
def num_in_rect(rw, rh, s):
    n_in_w = rw//s
    n_in_h = rh//s
    n_in_r = n_in_h * n_in_w
    return None

# fill an X by Y rectangle with the squares. Form a bottom layer from left
# to right, then build on top of it.
def fill_X_by_Y(X, Y, L):
    if X == 0 or Y == 0:
        return L
    can_fit = False
    for Li in L.keys():
        if Li <= min(X, Y):
            can_fit = True
            break
    if not can_fit:
        return L
    n_in_w = X//Li
    n_in_h = Y//Li
    n_can_fit = n_in_w * n_in_h
    n_did_fit = min(n_can_fit, L[Li])
    L[Li] -= n_did_fit
    L = +L # remove 0 and negative counts
    # does upper gap exist?
    # n_layer BUGGED
    n_layer = math.ceil(n_did_fit/n_in_w)
    if n_layer*Li < Y:
        upper_h = Y - n_layer*Li
    else:
        upper_h = 0
    # does middle gap exist?
    n_in_last_lyr = n_did_fit%n_in_w
    if n_in_last_lyr != 0:
        middle_w = X - n_in_last_lyr*Li
    else:
        middle_w = 0
    # does lower gap exist?
    if n_did_fit >= n_in_w and n_in_w*Li < X:
        lower_w = X - n_in_w*Li
    else:
        lower_w = 0
    # lower_gap
    L = fill_X_by_Y(lower_w, Li, L)
    # middle_gap
    L = fill_X_by_Y(middle_w, Li, L)
    # upper_gap
    L = fill_X_by_Y(X, upper_h, L)
    L = +L
    return L
    

def solve(N, M, L):
    n_req = 0
    while L != col.Counter():
        L = fill_X_by_Y(M, M, L)
        n_req += 1
    return n_req

def main():
    ncases = int(input())
    for case in range(1, ncases+1):
        # if case == 3:
        #     breakpoint()
        words = input().split()
        N, M = int(words[0]), int(words[1])
        # side lengths
        L = [2**int(Si) for Si in words[2:]]
        L.sort(reverse=True)
        # dict insertion order is preserved.
        L = col.Counter(L)
        nbuy = solve(N, M, L)
        print(f"Case #{case}: {nbuy}")

if __name__ == "__main__":
    main()