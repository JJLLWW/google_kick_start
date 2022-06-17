# tel, turb, room color coded,

# tel: can go from room of color x to another room of color x
# turb: directed edge from room a to b.

# get 1 <= S <= 100 "soldiers"

# colored directed weighted graph, compress nodes with same color into single nodes.
# now can find shortest path between any pair of nodes using Dijkstra's algorithm.

# weighted directed edge
class wdedge:
    def __init__(self, src, dest, w):
        self.src = src
        self.dest = dest
        self.w = w

# this is the compressed graph
class wdgraph:
    def __init__(self):
        # color from index, indeces from color
        self.cfi = dict()
        self.ifc = dict()
        self.nodes = set()
        self.adj = dict()
        self.adjw = dict()
    def add_node(self, i, col):
        self.nodes.add(col)
        self.adj[col] = set()
        # ti <= 1000
        self.adjw[col] = float("inf")
        self.cfi[i] = col
        if col not in self.ifc.keys():
            self.ifc[col] = [i]
        else:
            self.ifc[col].append(i)
    def add_edge(self, i_src, i_dest, w):
        c_from, c_to = self.cfi(i_src), self.cfi(i_dest)
        self.adj[c_from].add(c_to)
        if w < self.adjw[c_from]:
            self.adjw[c_from] = w
    # use Dijsktra's algorithm to get the shortest dist
    def min_dist(self, i, j):
        ci, cj = self.cfi(i), self.cfi(j)
        dists = dict()
        for v in self.nodes:
            dists[v] = float("inf")
        Q = self.nodes
        dists[i] = 0
        while len(Q) != 0:
            u = min(dists)
            Q.remove(u)
            for v in self.adj[u]:
                if v in Q:
                    pass
        

def main():
    T = int(input())
    for case in range(1, T+1):
        N = int(input())
        g = wdgraph()
        for i in range(1, N+1):
            col = input()
            g.add_node(i, col)
        M = int(input())
        for _ in range(M):
            words = input().split()
            a, b, t = [int(word) for word in words]
            g.add_edge(a, b, t)
        S = int(input())
        sols = []
        for _ in range(S):
            words = input().split()
            p, q = [int(word) for word in words]
            sols.append([p, q])
        print(f"Case #{case}:")
        for p, q in sols:
            d = g.min_dist(p, q)
            print(d)

main()