def solve(P, I):
    n_ops, j = 0, 0
    for i in range(len(P)):
        # if we have already matched all characters of I, just delete all remaing members of P.
        if j >= len(I):
            n_ops += len(P) - i
            break
        elif P[i] == I[j]:
            j += 1
        else:
            n_ops += 1
    # I = "abc", if all matched j == 3, otherwise j < 3.
    return None if j < len(I) else n_ops

def main():
    ncases = int(input())
    for case in range(1, ncases+1):
        I = input()
        P = input()
        n_ops = solve(P, I)
        if n_ops == None:
            print(f"Case #{case}: IMPOSSIBLE")
        else:
            print(f"Case #{case}: {n_ops}")

if __name__ == "__main__":
    main()

# I -> P. P is mangled I, need to remove letters from I to get P

# Strategy: only delete characters if they don't match a (X)a b (X)b (X)b <-> ab

# P=ab I=ab12345 -> len(P)=2, len(I) = 7