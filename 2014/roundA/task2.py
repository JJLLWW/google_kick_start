# digit displayed by 7 segments. A single "display" is just the 7 segments.
# segments labelled A - B - ... - G.

# Get given a list of N states as 7 digit binary strings, digit i 0/1 means segment
# i is on/off respectively.

# each state is some 1 digit number [0-9], states are a cyclically decreasing sequence
# of numbers.

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

def solve(states, N):
    # we know a segment that is active in any state must be working.
    working = or_all(states)
    # we can gradually infer which segments are broken
    broken = 0
    broken_old = None
    # pos_vals[i] possible values state i could represent
    pos_vals = [set() for i in range(N)]
    pos_vals_old = None
    # when to break out? will this always only take 1 pass? THIS MAY BE BUGGED
    while pos_vals != pos_vals_old and broken != broken_old:
        for i in range(N):
            pos_vals[i] = get_pos_vals(states[i], working)
            # remove those inconsistent with the last obtained values
            if i != 0:
                rm_vals, rm_vals_prev = [], []
                for val in pos_vals[i]:
                    if val+1 not in pos_vals[i-1]:
                        rm_vals.append(val)
                for val in pos_vals[i-1]:
                    if val-1 not in pos_vals[i]:
                        rm_vals_prev.append(val)
                for rval in rm_vals:
                    pos_vals[i].remove(rval)
                for rval in rm_vals_prev:
                    pos_vals[i-1].remove(rval)
            # may be no possible values, don't want to continue.
            if pos_vals[i] == set():
                return None
            # deduce if any more segments are broken, if a segment not equal
            # to a known working one is on in all possible values, then that segment
            # must be broken.
            on_in_all = and_all_dig(pos_vals[i])
            # this need not be positive (BUGGED)
            new_on = on_in_all & ~working
            broken_old = broken
            broken |= new_on
            pos_vals_old = pos_vals
        # we may still not have enough information to determine the next digits value
        for pval_set in pos_vals:
            if len(pval_set) > 1:
                return None
        next_val = pos_vals[-1].pop() - 1
        nv_state = state_dig[next_val]
        known_bits = working | broken
        # even if we know the next value, if we don't know whether a segment needed to 
        # represent it is working or broken we don't know how to represent it.
        if known_bits & nv_state != nv_state:
            return None
        else:
            # does this work?
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

main()