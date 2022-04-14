def get_digits(n):
    # get the digits of n, most significant first.
    dig = []
    while n != 0:
        dig.append(n%10)
        n //= 10
    dig.reverse()
    return dig

def int_from_dig(dig):
    i, res = 0, 0
    for d in reversed(dig):
        res += d*(10**i)
        i += 1
    return res

def solve(N):
    # this kind of works, but isn't fast enough for test set 2.
    dig = get_digits(N)
    res = None
    # what if N itself is a multiple of 9, do we HAVE to add a digit?
    for i in range(len(dig)+1):
        for num in range(10):
            # no leading zeroes
            if i == 0 and num == 0:
                continue
            dig.insert(i, num)
            val = int_from_dig(dig)
            if val % 9 == 0:
                if res == None or val < res:
                    res = val
            del(dig[i])
    return res

def main():
    ncases = int(input())
    for case in range(1, ncases+1):
        N = int(input())
        M = solve(N)
        print(f"Case #{case}: {M}")

if __name__ == "__main__":
    main()

# pos integer N, construct a number M that is a multiple of 9 by adding one digit in N.
# smallest such M

# 10^123456 -> 123456 digits -> 1234567 places for the new digit -> 9 options for the digit.