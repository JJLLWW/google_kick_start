# N*N grid of cells, cell wall "#", exit (?), or empty ".", can we solve the maze in <= 10,000 steps?

# move N (up), S (down), E (left), W (right) one square (no diag), will always have hand on left wall, turns clockwise

# (!) which direction do we face on the first move? (!) belive its S 

# add NE, NW, SE, SW
turn90aclock = {"N" : "W", "E" : "N", "S" : "E",  "W" : "S"}
turn90clock = {"N" : "E", "E" : "S", "S" : "W", "W" : "N"}

# Assume facing South intiially, we may be enclosed on all sides.
def get_init_dir(maze, sx, sy):
    init_dir = "S"
    cur_dir = None
    # keep turning until we aren't facing a wall + hand on wall or have done a 360
    while cur_dir != init_dir:
        if cur_dir == None:
            cur_dir = init_dir
        fx, fy = move(cur_dir, sx, sy)
        lx, ly = move(turn90aclock[cur_dir], sx, sy)
        if maze[fy][fx] != "#" and maze[ly][lx] == "#":
            return cur_dir
        else:
            cur_dir = turn90clock[cur_dir]
    return None

# dir is the direction edison is facing
def get_dir(maze, px, py, dir):
    lh_dir = turn90aclock[dir]
    lx, ly = move(lh_dir, px, py)
    # follow wall around if lose touch
    if maze[ly][lx] != "#":
        return lh_dir
    nx, ny = move(dir, px, py)
    # we are walking into a wall and need to rotate around, we know we can't spin forever
    while maze[ny][nx] == "#":
        dir = turn90clock[dir]
        nx, ny = move(dir, px, py)
    return dir

# assume at this point we have checked we aren't walking into a wall
def move(dir, posx, posy):
    newx, newy = posx, posy
    if dir == "E":
        newx = posx + 1
    if dir == "W":
        newx = posx - 1
    if dir == "N":
        newy = posy - 1
    if dir == "S":
        newy = posy + 1
    return newx, newy

# small enough to just run through 10000 steps. assume always start with a wall to the left
def solve(sx, sy, ex, ey, maze):
    maxstep = 10000
    # first step, assume initially facing south, so hand to the east.
    dir = get_init_dir(maze, sx, sy)
    if dir == None:
        return None, None
    path = dir
    px, py = move(dir, sx, sy)
    nstep = 1
    while nstep < 10000:
        if px == ex and py == ey:
            return nstep, path    
        dir = get_dir(maze, px, py, dir)
        px, py = move(dir, px, py)
        path += dir
        nstep += 1
    if px == ex and py == ey:
        return nstep, path
    else:
        return None, None

def main():
    T = int(input())
    for case in range(1, T+1):
        N = int(input())
        maze = []
        # add surrounding walls to avoid index conversion + treating edges of the maze seperately
        maze.append("#"*(N+2))
        for _ in range(N):
            line = input()
            maze.append("#" + line + "#")
        words = input().split()
        maze.append("#"*(N+2))
        sy, sx, ex, ey = int(words[0]), int(words[1]), int(words[2]), int(words[3])
        # something screwy is going on with the coordinates + am I sure we're intially facing south?
        nstep, path = solve(sx, sy, ey, ex, maze)
        if path is None:
            print(f"Case #{case}: Edison ran out of energy.")
        else:
            print(f"Case #{case}: {nstep}")
            print(path)

main()