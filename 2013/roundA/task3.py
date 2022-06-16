# assume every rational only occurs once
def solve_prob1(n):
    # if n = 100101 in binary, this corresponds to LLRLR in the tree, non-leading digit 0 => L, 1 => R.
    moves = []
    while n > 1:
        if n%2 == 0:
            moves.append("L")
        else:
            moves.append("R")
        n//=2
    moves.reverse()
    p, q = 1, 1
    for move in moves:
        p_old, q_old = p, q
        if move == "L":
            p, q = p_old, p_old + q_old
        elif move == "R":
            p, q = p_old + q_old, q_old
    return p, q

def solve_prob2(p, q):
    # use problem 1s observation we can get n from the LR sequence, and that we can apply the procedure in reverse.
    moves = []
    while p != q:
        p_old, q_old = p, q
        # last move was L
        if p < q:
            moves.append("L")
            p, q = p_old, q_old - p_old
        elif p > q:
            moves.append("R")
            p, q = p_old - q_old, q_old
    n = 0
    for i in range(len(moves)):
        bin_dig = 0 if (moves[i] == "L") else 1
        n += bin_dig*(2**i)
    n += 2**len(moves)
    return n

def main():
    ncases = int(input())
    for case in range(1, ncases+1):
        words = input().split()
        pid = int(words[0])
        if(pid == 1):
            n = int(words[1])
            p, q = solve_prob1(n)
            print(f"Case #{case}: {p} {q}")
        else:
            p, q = int(words[1]), int(words[2])
            n = solve_prob2(p, q)
            print(f"Case #{case}: {n}")
main()