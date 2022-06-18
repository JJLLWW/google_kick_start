# get NxM (N row, M col) grid of cells, tl is (0,0), br is (N-1,M-1).
# cells either danger "-1" or some +ve integer power p (can only collect from a cell once)
# entrance and exit cells distinct and both safe.
# move up, down, left, right.

# of the shortest paths, choose the one with the maximum power.

# expand out from en until reach ex, label cells 0 to NSTEP based on which step they were first
# visited. As we want shortest number of steps, these cells' weights are the least weights obtained
# at this stage

# 2x3
# 0<=x<=N and 0<=y<=M (0,0) (0,1) (0,2) OR (0,0) (1,0) (2,0)  0<=x<=M and 0<=y<=N
#                     (1,0) (1,1) (1,2) ?? (0,1) (1,1) (2,1)

# need a custom __eq__ for in to work with a list of these objects
class pt:
    def __init__(self, x, y):
        self.x, self.y = x, y
    def __eq__(self, other):
        return (self.x == other.x) and (self.y == other.y)
    def __hash__(self):
        return hash(repr(self))
    def __repr__(self):
        return "(" + str(self.x) + ", " +  str(self.y) + ")"

def get_nbrs(maze, M, N, p):
    nbrs = []
    if 0 <= p.x + 1 < N and maze[p.x+1][p.y] != -1:
        nbrs.append(pt(p.x+1, p.y))
    if 0 <= p.x - 1 < N and maze[p.x-1][p.y] != -1:
        nbrs.append(pt(p.x-1, p.y))
    if 0 <= p.y + 1 < M and maze[p.x][p.y+1] != -1:
        nbrs.append(pt(p.x, p.y+1))
    if 0 <= p.y - 1 < M and maze[p.x][p.y-1] != -1:
        nbrs.append(pt(p.x, p.y-1))
    return nbrs

# we want the MAXIMUM weight path
def solve(maze, M, N, en, ex):
    # do a BFS to get all shortest paths
    wghts = [[float("-inf")]*M for _ in range(N)] 
    dist = [[None]*M for _ in range(N)]
    dist[en.x][en.y], wghts[en.x][en.y] = 0, maze[en.x][en.y]
    cur_dist = 0
    pts = set()
    pts.add(en)
    # break out if we've got the endpoint or no new points.
    while True:
        new_pts = set()
        for pt in pts:
            nbrs = get_nbrs(maze, M, N, pt)
            for p in nbrs:
                # have we already visited this point? what if it gets visited multiple times, we still want multiple prevs
                if dist[p.x][p.y] == None or dist[p.x][p.y] == cur_dist+1:
                    new_pts.add(p)
                    dist[p.x][p.y] = cur_dist+1
                    w = wghts[pt.x][pt.y] + maze[p.x][p.y]
                    if w > wghts[p.x][p.y]:
                        wghts[p.x][p.y] = w
        cur_dist += 1
        pts = new_pts
        # we found the exit
        if ex in new_pts:
            break
        # we have failed to reach the exit
        if new_pts == set():
            return None
    w = wghts[ex.x][ex.y]
    return w

def main():
    ncases = int(input())
    for case in range(1, ncases+1):
        words = input().split()
        N, M = [int(word) for word in words]
        words = input().split()
        en_x, en_y, ex_x, ex_y = [int(word) for word in words]
        en, ex = pt(en_x, en_y), pt(ex_x, ex_y)
        maze = []
        for _ in range(N):
            words = input().split()
            ints = [int(word) for word in words]
            maze.append(ints)
        res = solve(maze, M, N, en, ex)
        if res == None:
            print(f"Case #{case}: Mission Impossible.")
        else:
            print(f"Case #{case}: {res}")

main()