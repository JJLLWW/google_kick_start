# another 2D grid. (N, W, E, S), dist (x1, y1) to (x2, y2) is |x1-x2| + |y1-y2|

# rectangular areas (x1, y1, x2, y2), filled with integer points. Given several rectangles.

# choose a selected point with minimal sum of all distances from other points to that point.
# if multiple must be the one with the smallest x, if multiple smallest x, additionally one with
# smallest y.

# rectangles DO NOT INTERSECT

# strategy: for every rectangle, we compress all other rectangles to a line/point
# that can be moved up/down or left/right into the desired rectangle. Once all
# other rectangles moved together, then calculate the best point in the "weighted"
# rectangle by considering dx and dy seperately (weight is number of points moved to
# that point from other rectangles.)

class rect():
    def __init__(self, x1, y1, x2, y2):
        self.x1, self.x2, self.y1, self.y2 = x1, x2, y1, y2
        self.wght = [[1]*(x2 - x1 + 1)]*(y2 - y1 + 1)
    def __repr__(self):
        s = f"(({self.x1}, {self.x2}), ({self.y1}, {self.y2}))"
        return s
    # assume oth is a rectangle inside self
    def add(self, oth):
        for x in range(oth.x1, oth.x2+1):
            for y in range(oth.y1, oth.y2+1):
                self.wght[x][y] += oth.wght[x][y]
    def squash_into_x(self, x1, x2):
        n_mov = 0
        if self.x2 < x1:
            self.x1 = self.x2 = x1
        elif self.x1 > x2:
            self.x1 = self.x2 = x2
        elif self.x1 < x1 and self.x2 > x2:
            self.x1, self.x2 = x1, x2
        return n_mov
    # move rect oth onto self.
    def move_rect_to(self, oth):
        w_oth = rect(oth.x1, oth.y1, oth.x2, oth.y2)
        n_mov = 0
        n_mov += w_oth.squash_into_x(self.x1, self.x2)
        self.add(w_oth)
        return n_mov
    def find_optimum(self):
        return 0, 0, 0

def solve(rects):
    # solution with minimal x, then minimal y
    x, y, d = float("inf"), float("inf"), float("inf")
    for rec in rects:
        x_cur, y_cur, d_cur = None, None, None
        wrect = rect(rec.x1, rec.y1, rec.x2, rec.y2)
        for oth_r in rects:
            if oth_r == rec:
                continue
            # distance from moving all points into this rectangle
            d_cur += wrect.move_rect_to(oth_r)
            # distance from moving all (weighted) points to the optimal point
            x_cur, y_cur, D = wrect.find_optimum()
            d_cur += D
        if d_cur <= d and x_cur<=x and y_cur <= y:
            x, y, d = x_cur, y_cur, d_cur
    return 0, 0, 0

def main():
    ncases = int(input())
    for case in range(1, ncases+1):
        B = int(input())
        rects = []
        for _ in range(B):
            words = input().split()
            x1, y1, x2, y2 = [int(word) for word in words]
            rects.append(rect(x1, y1, x2, y2))
        x, y, d = solve(rects)
        print(f"Case #{case}: {x} {y} {d}")

main()