# 9x9 grid, all rows, cols and 3x3 subgrids contain all digs from 1 to 9

# get COMPLETED grid, need to test whether a valid sol.
# given N*N grid, need rows, cols, NxN subgrids to contain all digs from 1 to N

def is_sol(grid, N):
    all = set()
    for i in range(1, N**2+1):
        all.add(i)
    # check rows
    for i in range(N**2):
        seen = set()
        for j in range(N**2):
            seen.add(grid[i][j])
        if seen != all:
            return False
    # check columns
    for i in range(N**2):
        seen = set()
        for j in range(N**2):
            seen.add(grid[j][i])
        if seen != all:
            return False
    # check subgrids
    for I in range(N):
        for J in range(N):
            tl_i, tl_j = I*N, J*N
            seen = set()
            for i in range(tl_i, tl_i + N):
                for j in range(tl_j, tl_j + N):
                    seen.add(grid[i][j])
            if seen != all:
                return False
    return True

def main():
    ncases = int(input())
    for case in range(1, ncases+1):
        N = int(input())
        grid = []
        for _ in range(N**2):
            words = input().split()
            line = [int(word) for word in words]
            grid.append(line)
        res = is_sol(grid, N)
        if res:
            print(f"Case #{case}: Yes")
        else:
            print(f"Case #{case}: No")
        

main()