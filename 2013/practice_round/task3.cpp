#include <iostream>
#include <vector>
#include <string>
#include <unordered_map>
#include <algorithm>

// split a group of 2M into two (not necessarily equally sized?) groups with 
// no pairs in common.

// if the graph is bipartite this is possible, if the graph is not bipartite this
// is impossible. (bipartiteness can be detected in quadratic time.)

// do a bfs in each connected component, coloring neighbouring vertices oppositely
// to the current vertex.

struct node {
    int node_idx;
    std::vector<int> adj;
};

class graph {
    private:
        std::vector<node> _nodes;
        std::vector<bool> _cols; // colours of each node
        std::unordered_map<std::string, int> _idx_map;
        int _cur_idx;
        bool bfs(std::vector<bool>& visited, int idx, bool col) {
            visited[idx] = true;
            _cols[idx] = col;
            for(int i: _nodes[idx].adj) {
                if(!visited[i]) {
                    if(!bfs(visited, i, !col)) {
                        return false;
                    }
                }
                else {
                    if(!col != _cols[i]) {
                        return false;
                    }
                }
            }
            return true;
        }
    public:
        graph() : _nodes{std::vector<node>()}, _cur_idx{0} {}
        void add_node(std::string& name) {
            if(_idx_map.count(name) != 0) {
                return;
            }
            _idx_map[name] = _cur_idx;
            _nodes.push_back({_cur_idx, std::vector<int>()});
            _cols.push_back(false);
            _cur_idx++;
        }
        void add_edge(std::string& name1, std::string& name2) {
            int i = _idx_map[name1], j = _idx_map[name2];
            _nodes[i].adj.push_back(j);
            _nodes[j].adj.push_back(i);
        }
        bool is_bipartite() {
            // BFS on each component O(V+E)
            std::vector<bool> visited(_nodes.size());
            std::fill(visited.begin(), visited.end(), false);
            while(!std::all_of(visited.begin(), visited.end(), [](bool b){ return b; })) {
                int idx;
                // std::first_of + iterator -> index simpler?
                for(idx=0; idx<visited.size(); idx++) {
                    if(!visited[idx]) {
                        break;
                    }
                }
                // see if the next connected component is bipartite.
                if(!bfs(visited, idx, false))
                    return false;
            }
            return true;
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
    bool is_bip = members.is_bipartite();
    return is_bip ? "Yes" : "No";
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