#!/usr/bin/python3

import task2

def main():
    l = [set([0]), set([9])]
    print(l)
    task2.rm_bad_vals(1, l)
    print(l)

main()