# get NxM (N row, M col) grid of cells, tl is (0,0), br is (N-1,M-1).
# cells either danger "-1" or some +ve integer power p (can only collect from a cell once)
# entrance and exit cells distinct and both safe.
# move up, down, left, right.

# of the shortest paths, choose the one with the maximum power.

# need to get ALL shortest paths from entrance to exit, BFS and don't go one step deeper once a
# path of length i is found.

import queue

def get_nbrs(maze, M, N, px, py):
    return None

def solve(maze, M, N, en_x, en_y, ex_x, ex_y):
    # do a BFS to get all shortest paths
    pts = queue.Queue()
    seen = [[False]*M]*N
    seen[en_x][en_y] = True
    pts.put([en_x, en_y, 0])
    stop = False
    # iterative BFS, how to record path?
    while pts.qsize() != 0 and not stop:
        pt_x, pt_y, lvl = pts.get()
        nbrs = get_nbrs(maze, M, N, pt_x, pt_y)
        for nbr_x, nbr_y in nbrs:
            if not seen[nbr_x][nbr_y]:
                seen[nbr_x][nbr_y] = True
                pts.put([nbr_x, nbr_y, lvl+1])

    return None

def main():
    ncases = int(input())
    # this may be necessary 
    for case in range(1, ncases+1):
        words = input().split()
        N, M = [int(word) for word in words]
        words = input().split()
        en_x, en_y, ex_x, ex_y = [int(word) for word in words]
        maze = []
        for _ in range(N):
            words = input().split()
            ints = [int(word) for word in words]
            maze.append(ints)
        res = solve(maze, M, N, en_x, en_y, ex_x, ex_y)
        if res == None:
            print(f"Case #{case}: Mission Impossible.")
        else:
            print(f"Case #{case}: {res}")

main()