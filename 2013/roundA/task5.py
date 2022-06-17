# tel, turb, room color coded,

# tel: can go from room of color x to another room of color x
# turb: directed edge from room a to b.

# get 1 <= S <= 100 "soldiers"

# strategy part 1, compress groups of rooms that are the same color into single rooms.

# colors from room, rooms from color
cfr = dict()
rfc = dict()

def add_room(i, col):
    if col not in rfc.keys():
        rfc[col] = [i]
    else:
        rfc[col].append(i)

def add_edge(list, a, b, t):
    if list[a] == None:
        list[a] = [(b, t)]
    else:
        list[a].append((b, t))

# there may be multiple edges from different compressed nodes, but we only care about 1 which
# is <= all others.
def compress_edges(WEO):
    WEC = dict()
    for i in range(len(WEO)):
        if WEO != None:
            for j, t in WEO:
                s, e = cfr[i], cfr[j]
                if (s, e) not in WEC.keys():
                    WEC[(s,e)] = t
                elif t < WEC[(s,e)]:
                    WEC[(s,e)] = t
    return WEC

def solve(WEO, sols):
    # first we need to get weighted edges from original rooms into weighted edges
    # from compressed nodes + convert dest and output nodes into colors.
    WEC = compress_edges(WEO)
    # We might as well run Dijsktras algorithm on the entire graph at all times.

    return None    

def main():
    T = int(input())
    for case in range(1, T+1):
        N = int(input()) # num rooms from 1 to N
        # room colors, strings len 1 or 2 consisting of a-z and 0-9
        tlifts, sols = [], []
        for i in range(N):
            col = input()
            cfr[i] = col
            add_room(i, col)
        M = int(input()) # num turbolifts
        # weighted (directed) edges, between different nodes of the original graph, WE[1] = [(2, t), (3, T)]
        # if directed edge from 1 to 2 with time t + directed edge from 1 to 3 with time T
        WEO = [None]*(N+1)
        for _ in range(M):
            words = input().split()
            a, b, t = [int(word) for word in words]
            add_edge(WEO, a, b, t)
        S = int(input()) # num soldiers
        for _ in range(S):
            words = input().split()
            p, q = [int(word) for word in words]
            sols.append((p, q))
        times = solve(WEO, sols)
        print(f"Case #{case}:")
        for time in times:
            print(time)

main()