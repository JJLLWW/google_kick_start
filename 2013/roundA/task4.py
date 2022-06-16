# N*N grid of cells, cell wall "#", exit (?), or empty ".", can we solve the maze in <= 10,000 steps?

# move N (up), S (down), E (left), W (right) one square (no diag), will always have hand on left wall, turns clockwise

# (!) which direction do we face on the first move? (!) belive its S 

# small enough to just run through 10000 steps. assume always start with a wall to the left
def solve(sx, sy, ex, ey):
    maxstep = 10000
    # first step, assume initially facing south, so hand to the east.
    dirs = ["E", "S", "W", "N"]
    nstep, path = 0, ""
    posx, posy = sx, sy
    while nstep <= 10000:
        if posx == ex and posy == ey:
            return nstep, path
    return None

# indeces are from top left (1,1), does it make sense to expand the maze into a (N+2)*(N+2) grid?
def main():
    T = int(input())
    for case in range(1, T+1):
        N = int(input())
        maze = []
        for _ in range(N):
            line = input()
            maze.append(line)
        words = input().split()
        # convert to zero indexed.
        sx, sy, ex, ey = int(words[0])-1, int(words[1])-1, int(words[2])-1, int(words[3])-1
        nstep, path = solve(sx, sy, ex, ey)
        if path is None:
            print(f"Case #{case}: Edison ran out of energy.")
        else:
            print(f"Case #{case}: {nstep}")
            print(path)

main()