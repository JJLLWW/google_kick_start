#!/usr/bin/python3

import task2

def main():
    l = [{8, 7, 6}, {6, 5}, {4}]
    print(l)
    task2.rm_bad_vals(l, 3)
    print(l)

main()