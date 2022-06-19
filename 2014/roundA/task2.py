# digit displayed by 7 segments. A single "display" is just the 7 segments.
# segments labelled A - B - ... - G.

# Get given a list of N states as 7 digit binary strings, digit i 0/1 means segment
# i is on/off respectively.

# each state is some 1 digit number [0-9], states are a cyclically decreasing sequence
# of numbers.

import functools as ft

# each digit 0-9 as a state
state_dig = [
    # 0 - ABCDEF - 0b1111,110
    0b1111110,
    # 1 - BC
    0b0110000,
    # 2 - ABGED - ABDEG
    0b1101101,
    # 3 - ABGCD - ABCDG
    0b1111001,
    # 4 - BGFC - BCFD
    0b0111010,
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

# can get the correct number but doesn't represent it as bars correctly.
# need to also figure out which segments are working or broken.
def solve(states):
    # get a bitmask of all segments we know are working
    working = ft.reduce(lambda x, y: x|y, states)
    broken = 0 # segments we KNOW are broken.
    valid_nums = []
    # possible values for this state.
    pos_vals = [i for i in range(10)]
    for state in states:
        valid = []
        # do the segments of this integer match what we know we have from the
        # known working segments?
        seen = working & state
        for i in pos_vals:
            if seen == state_dig[i] & working:
                valid.append(i)
        if valid == []:
            return None
        pos_vals = [(v-1)%10 for v in valid]
        valid_nums.append(valid)
        # bitmask of segments which should be on for all possible values.
        common = ft.reduce(lambda x, y: x&y, valid)
        new_working = common & state
        new_broken = common & (~state)
        print(bin(new_working), bin(new_broken))
        working |= new_working
        broken |= new_broken
    print(valid_nums, bin(working), bin(broken))
    if len(valid_nums[-1]) > 1:
        return None
    else: # unique sol
        val = (valid_nums[-1][0] - 1)%10
        print(val)
        val_as_state = state_dig[val]
        # we don't have enough information to know how this value will be represented
        if val_as_state & (working | broken) != val_as_state:
            return None
        else:
            return val_as_state & working

def main():
    ncases = int(input())
    for case in range(1, ncases+1):
        words = input().split()
        N = int(words[0])
        states = []
        for word in words[1:]:
            states.append(int(word, base=2))
        res = solve(states)
        if res is None:
            print(f"Case #{case}: ERROR!")
        else:
            print(f"Case #{case}: {bin(res)[2:]}")

main()