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

# this is the compressed graph, once get num nodes, just store the distance between each in
# a 2D table, inf if no edge.
class wdgraph:
    def __init__(self):
        # color from index, indeces from color
        self.cfi = dict()
        self.ifc = dict()
        self.nodes = set()
        self.adj = dict()
        self.edgew = dict()
    def add_node(self, i, col):
        self.nodes.add(col)
        self.adj[col] = set()
        self.cfi[i] = col
        if col not in self.ifc.keys():
            self.ifc[col] = [i]
        else:
            self.ifc[col].append(i)
    def init_weights(self):
        for c1 in self.ifc.keys():
            for c2 in self.ifc.keys():
                self.edgew[(c1, c2)] = float("inf")
    # ??
    def add_edge(self, i_src, i_dest, w):
        c_from, c_to = self.cfi[i_src], self.cfi[i_dest]
        self.adj[c_from].add(c_to)
        if w < self.edgew[(c_from, c_to)]:
            self.edgew[(c_from, c_to)] = w
    def log(self):
        print(self.nodes, self.edgew, self.adj)
    # use Dijsktra's algorithm to get the shortest dist
    def min_dist(self, i, j):
        ci, cj = self.cfi[i], self.cfi[j]
        dists = dict()
        Q = set()
        for v in self.nodes:
            dists[v] = float("inf")
            Q.add(v)
        dists[ci] = 0
        while len(Q) != 0:
            # get vertex with min dist in Q
            u, dst = None, float("inf")
            for v in Q:
                if dists[v] <= dst:
                    u, dst = v, dists[v]
            Q.remove(u)
            for v in self.adj[u]:
                if v in Q:
                    alt = dists[u] + self.edgew[(u, v)]
                    if alt < dists[v] and dists[u] != float("inf"):
                        dists[v] = alt
        d = dists[cj] if dists[cj] != float("inf") else -1
        return d  

def main():
    T = int(input())
    for case in range(1, T+1):
        N = int(input())
        g = wdgraph()
        for i in range(1, N+1):
            col = input()
            g.add_node(i, col)
        g.init_weights()
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