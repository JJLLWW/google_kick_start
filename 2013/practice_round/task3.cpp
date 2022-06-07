#include <iostream>
#include <vector>
#include <string>
#include <unordered_map>
#include <algorithm>

// split a group of 2M into two (not necessarily equally sized?) groups with 
// no pairs in common.

// is a graph connected (impossible), or disconnected (possible).
// for an undirected graph, finding connected components with BFS/DFS is O(V+E)

// how to represent the graph? Every node needs to know adjacent nodes.

struct node {
    int node_idx;
    std::vector<int> adj;
};

class graph {
    private:
        std::vector<node> _nodes;
        std::unordered_map<std::string, int> _idx_map;
        int _cur_idx;
        void bfs(std::vector<bool>& visited, int idx) {
            // do a bfs
            visited[idx] = true;
            for(int i: _nodes[idx].adj) {
                if(!visited[i]) {
                    bfs(visited, i);
                }
            }
        }
    public:
        graph() : _nodes{std::vector<node>()}, _cur_idx{0} {}
        void add_node(std::string& name) {
            if(_idx_map.count(name) != 0) {
                return;
            }
            _idx_map[name] = _cur_idx;
            _nodes.push_back({_cur_idx, std::vector<int>()});
            _cur_idx++;
        }
        void add_edge(std::string& name1, std::string& name2) {
            int i = _idx_map[name1], j = _idx_map[name2];
            _nodes[i].adj.push_back(j);
            _nodes[j].adj.push_back(i);
        }
        int n_connected_comp() {
            // BFS on each component O(V+E)
            std::vector<bool> visited(_nodes.size());
            std::fill(visited.begin(), visited.end(), false);
            int n_comp = 0;
            while(!std::all_of(visited.begin(), visited.end(), [](bool b){ return b; })) {
                int idx;
                // std::first_of + iterator -> index simpler?
                for(idx=0; idx<visited.size(); idx++) {
                    if(!visited[idx]) {
                        break;
                    }
                }
                bfs(visited, idx);
                n_comp++;
            }
            return n_comp;
        }
};

// RVO
graph read_input() {
    int M;
    std::cin >> M;
    graph members;
    std::string name1, name2;
    for(int i=0; i<M; i++) {
        std::cin >> name1 >> name2;
        members.add_node(name1);
        members.add_node(name2);
        members.add_edge(name1, name2);
    }
    return members;
}

std::string solve(graph& members) {
    int n_comp = members.n_connected_comp();
    return (n_comp == 1) ? "No" : "Yes";
}

int main() {
    int ncases;
    std::cin >> ncases;
    for(int i=1; i<=ncases; i++) {
        graph members = read_input();
        std::string possible = solve(members);
        std::cout << "Case #" << i << ": " << possible << std::endl;
    }
}