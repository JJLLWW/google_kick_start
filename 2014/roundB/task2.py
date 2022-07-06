#!/usr/bin/python3

# New Years Eve

# triangular pyramid of glasses, each horizontal plane a level.
# Levels numbered from 1 (highest) to 2, 3, 4, ...
# In each level glasses numbered from 1 to L*(L+1)/2

# each glass holds 250ml, when full overflows equally into the 3 glasses below it.

# B bottles 750ml each poured (into the top glass?)

# need num ml y in glass L, N.

# what are the indeces of the 3 glasses (T, BL, BR) below a glass on level l with index i?
# T has index i, BL has index "i + len_i_row - 1", BR has index "i + len_i_row" 

# every glass on the same level will not have the same ml.

import copy

CAPACITY_BOT = 750
CAPACITY_GLASS = 250

def get_sz_layer(l):
    return l*(l+1)//2

def get_row_width_glass_n(n):
    width = 1
    # if on a row of size w, it would not be a valid index on layer w-1 but would be valid on layer w
    while n > get_sz_layer(width):
        width += 1
    return width

# get the indeces of the glasses on layer l+1 a glass at pos n on layer l will overflow into.  
def get_base_idxs(n):
    top_n = n
    w_row = get_row_width_glass_n(n)
    bot_left_n = n + w_row
    bot_right_n = bot_left_n + 1
    return [top_n, bot_left_n, bot_right_n]

# simulate what will happen
def solve(B, L, N):
    base_sz = get_sz_layer(L)
    cur_layer_ml = [0]*(base_sz+1)
    next_layer_ml = [0]*(base_sz+1)
    n_ml = B*CAPACITY_BOT
    cur_layer_ml[1] = n_ml
    for l in range(1,L):
        next_layer_ml = [0]*(base_sz+1)
        for n in range(1, get_sz_layer(l)+1):
            oflow = cur_layer_ml[n] - CAPACITY_GLASS
            if oflow > 0:
                oflow_each = oflow/3
                idxs = get_base_idxs(n)
                for m in idxs:
                    next_layer_ml[m] += oflow_each
        # cur layer is next layer
        cur_layer_ml = copy.copy(next_layer_ml)
    # the glass may be overflowing itself, if it is we just return its capacity
    ml_in_glass = cur_layer_ml[N]
    if ml_in_glass > CAPACITY_GLASS:
        ml_in_glass = CAPACITY_GLASS
    return ml_in_glass

def main():
    ncases = int(input())
    for case in range(1, ncases+1):
        words = input().split()
        [B, L, N] = [int(word) for word in words]
        y = solve(B, L, N)
        # we want y outputed to 7 decimal places.
        print(f"Case #{case}: {y:.7f}")

main()