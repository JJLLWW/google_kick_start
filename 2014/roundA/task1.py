# NxN grid.

# move ALL tiles "left", "right", "up", "down" as far as they will go.
# if two tiles with the SAME NUMBER n collide in a move, they merge into one tile with
# value 2*n.

# given board state, need to get what it looks like after a single move.

# modify board in place
def solve(DIR, N, board):
    if DIR == "left":
        starts = [i*N for i in range(N)]
        step = 1
    elif DIR == "right":
        starts = [N-1 + i*N for i in range(N)]
        step = -1
    elif DIR == "up":
        starts = [i for i in range(N)]
        step = N
    elif DIR == "down":
        starts = [N*(N-1)+i for i in range(N)]
        step = -N
    for start in starts:
        # much easier to follow if do two passes even if approx. two times slower.
        line = []
        just_merged = False
        for i in range(N):
            idx = start + i*step
            if board[idx] == 0:
                continue
            if line == []:
                line.append(board[idx])
            elif board[idx] == line[-1] and not just_merged:
                line[-1] = 2*board[idx]
                just_merged = True
            else:
                just_merged = False
                line.append(board[idx])
        line += [0]*(N-len(line))
        for i in range(N):
            idx = start + i*step
            board[idx] = line[i]

def main():
    ncases = int(input())
    for case in range(1, ncases+1):
        words = input().split()
        N = int(words[0])
        DIR = words[1]
        # use a 1D index for the 2D array.
        board = []
        for _ in range(N):
            words = input().split()
            for i in range(N):
                board.append(int(words[i]))
        # modify board in place
        solve(DIR, N, board)
        print(f"Case #{case}:")
        for i in range(N**2):
            if i % N == N-1:
                print(board[i])
            else:
                print(f"{board[i]} ", end='')

main()