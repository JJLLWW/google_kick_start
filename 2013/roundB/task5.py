# NxN hexagonal board, two sides R and B, board starts empty, both sides place colored stones
# on any non-occupied square. Starting player is determined randomly (50-50)

# top + bottom sides of board R, left + right sides B. Square 'R', 'B' or '.'
# each interior square has 6 neighbours.

# indexed S[row][col].

# get given game state, tell whether it was valid and if it was who won.

# possible invalid states:
# 1) - the number of Bs nB and number of As differ by more than 1.
# 2) - both B and R have a winning path.
# 3) - B/R's last move was winning but R/B has one more stone than B/R
# 4) - Considering the graph of colored R/B paths from one side of the board to the other, this graph does not
#      have an articulation vertex (so the side would have won on the last move and kept playing.) 

#   B B B
# B B   B B - is still valid even though multiple paths, it's if there are multiple endpoints
#   B B B   - joined to a single endpoint.

# B B
#   B B - is also a valid winning configuration, blue could have started from the LHS.
# B B

#   B B
# B B   - ok as could have started from RHS
#   B B

# connected components of Bs? containing at least one start/end point. If a connected component contains 2 start pts 
# and 2 end pts we know the board configuration is impossible.

# all hexagons indexed from top left (0, 0)

# (0,0) (0,1)
# (1,0) (1,1)

class pt:
    def __init__(self, x, y):
        self.x, self.y = x, y
    def __repr__(self):
        return f"({self.x}, {self.y})"
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

# get neighbours of hexagon at point p, with color "R" if board is NxN
def get_nbrs(squares, p, N, match="R"):
    nbrs, ret_nbrs = [], []
    if 0 < p.x - 1 < N:
        nbrs += [pt(p.x-1, p.y)]
    if 0 < p.x + 1 < N:
        nbrs += [pt(p.x+1, p.y)]
    if 0 < p.y - 1 < N:
        nbrs += [pt(p.x, p.y-1)]
    if 0 < p.y + 1 < N:
        nbrs += [pt(p.x, p.y+1)]
    # extra hexagonal neighbours (x+1, y-1), (x-1, y+1)
    if 0 < p.x + 1 < N and 0 < p.y - 1 < N:
        nbrs += [pt(p.x+1, p.y-1)]
    if 0 < p.x - 1 < N and 0 < p.y + 1 < N:
        nbrs += [pt(p.x-1, p.y+1)]
    for n in nbrs:
        if squares[n.x][n.y] == match:
            ret_nbrs.append(n)
    return ret_nbrs

# we are in an impossible configuration if:
def get_nwon(squares, N, starts, ends, hor=False):
    side = "B" if hor else "R"
    ways = 0
    for start in starts:
        stack = [start]
        visited = []
        while stack != []:
            v = stack.pop()
            # found a path
            if v in ends:
                ways += 1
            if v not in visited:
                visited.append(v)
                nbrs = get_nbrs(squares, v, N, side)
                for n in nbrs:
                    stack.append(n)
        if ways > 1:
            return ways
    return ways

# returns number of ways blue has won wB, and number of ways red has won wR.
def get_ways_won(squares, N):
    wB, wR = 0, 0
    # top to bottom paths winning for red
    starts, ends = [], []
    for y in range(N):
        if squares[0][y] == "R":
            starts.append(pt(0, y))
        if squares[N-1][y] == "R":
            ends.append(pt(N-1, y))
    wR = get_nwon(squares, N, starts, ends, hor=False)
    starts, ends = [], []
    # left to right paths winning for blue
    for x in range(N):
        if squares[x][0] == "B":
            starts.append(pt(x, 0))
        if squares[x][N-1] == "B":
            ends.append(pt(x, N-1))
    wB = get_nwon(squares, N, starts, ends, hor=True)
    return wR, wB

def main():
    ncases = int(input())
    for case in range(1, ncases+1):
        N = int(input())
        nred, nblue = 0, 0
        squares = []
        for i in range(N):
            line = input()
            squares.append(line)
            for j in range(N):
                if line[j] == "R":
                    nred += 1
                elif line[j] == "B":
                    nblue += 1
        # Condition 1) for impossibility.
        if abs(nred - nblue) > 1:
            print(f"Case {case}: Impossible")
            continue
        wR, wB = get_ways_won(squares, N)
        if wB + wR > 1:
            print(f"Case {case}: Impossible")
        elif wB == 1:
            print(f"Case {case}: Blue wins")
        elif wR == 1:
            print(f"Case {case}: Red wins")
        else:
            print(f"Case {case}: Nobody wins")
            
main()