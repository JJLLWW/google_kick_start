#!/usr/bin/python3

# digit displayed by 7 segments. A single "display" is just the 7 segments.
# segments labelled A - B - ... - G.

# Get given a list of N states as 7 digit binary strings, digit i 0/1 means segment
# i is on/off respectively.

# each state is some 1 digit number [0-9], states are a cyclically decreasing sequence
# of numbers.

import copy
import functools as ft

# each digit 0-9 as a state, CHECK FOR MISTAKES
state_dig = [
    # 0 - ABCDEF - 0b1111,110
    0b1111110,
    # 1 - BC
    0b0110000,
    # 2 - ABGED - ABDEG
    0b1101101,
    # 3 - ABGCD - ABCDG
    0b1111001,
    # 4 - BGFC - BCFG
    0b0110011,
    # 5 - AFGCD - ACDFG
    0b1011011,
    # 6 - AFGDCE
    0b1011111,
    # 7 - ABC
    0b1110000,
    # 8 - (all)
    0b1111111,
    # 9 - (all but E)
    0b1111011
]

def cyclic_dec(x):
    return (x-1)%10

def cyclic_inc(x):
    return (x+1)%10

def or_all(l):
    return ft.reduce(lambda x, y: x|y, l)

def and_all_dig(l):
    return ft.reduce(lambda x, y: x&y, [state_dig[d] for d in l])

def get_pos_vals(state, working):
    pvals = set()
    for d in range(10):
        d_state = state_dig[d]
        # we can work out which bits should be on for this number.
        on_in_num = d_state & working
        on_in_state = state & working
        if on_in_num == on_in_state:
            pvals.add(d)
    return pvals

def rm_bad_adj(pos_vals, i):
    rm_vals, rm_vals_prev = [], []
    for val in pos_vals[i]:
        if cyclic_inc(val) not in pos_vals[i-1]:
            rm_vals.append(val)
    for val in pos_vals[i-1]:
        if cyclic_dec(val) not in pos_vals[i]:
            rm_vals_prev.append(val)
    for rval in rm_vals:
        pos_vals[i].remove(rval)
    for rval in rm_vals_prev:
        pos_vals[i-1].remove(rval)

def rm_bad_vals(pos_vals, N):
    if N == 1:
        return
    pos_vals_old = None
    while pos_vals != pos_vals_old:
        pos_vals_old = copy.deepcopy(pos_vals)
        for i in range(1,N):
            rm_bad_adj(pos_vals, i)

# If a segment not equal to a known working one is on in all possible values, then that segment
# must be broken.
def get_broken_segs(pos_vals, N, working):
    broken = 0
    for i in range(N):
        on_in_all = and_all_dig(pos_vals[i])
        new_on = on_in_all & ~working
        broken |= new_on
    return broken

def solve(states, N):
    # we know a segment that is active in any state must be working.
    working = or_all(states)
    # we can gradually infer which segments are broken
    broken_old = None
    # possible values each state (in isolation) could represent.
    pos_vals = [get_pos_vals(states[i], working) for i in range(N)]
    # remove obviously impossible values, eg. [{3}, {9}]
    rm_bad_vals(pos_vals, N)
    broken = get_broken_segs(pos_vals, N, working)
    # we may still not have enough information to determine the next digits value
    for pval_set in pos_vals:
        if len(pval_set) != 1:
            return None
    next_val = cyclic_dec(pos_vals[-1].pop())
    nv_state = state_dig[next_val]
    known_bits = working | broken
    # even if we know the next value, if we don't know whether a segment needed to 
    # represent it is working or broken we don't know how to represent it.
    if known_bits & nv_state != nv_state:
        return None
    else:
        return nv_state & working
        
def main():
    ncases = int(input())
    for case in range(1, ncases+1):
        words = input().split()
        N = int(words[0])
        states = []
        for word in words[1:]:
            states.append(int(word, base=2))
        res = solve(states, N)
        if res is None:
            print(f"Case #{case}: ERROR!")
        else:
            print(f"Case #{case}: {bin(res)[2:].zfill(7)}")

if __name__ == "__main__":
    main()