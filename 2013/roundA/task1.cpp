#include <iostream>
#include <vector>
#include <algorithm>

// books in some random order, each has an integer worth,  
// worth odd -> A, worth even -> B. Positions "labelled" depending
// on who owns the book initially on them.

// Alex's books should be in increasing order of worth.
// Bob's books should be in decreasing order of worth.

// RVO
std::vector<bool> read_input(std::vector<int>& books_A, std::vector<int>& books_B) {
    int N;
    std::cin >> N;
    std::vector<bool> pos_alex(N);
    for(int i=0; i<N; i++) {
        int worth;
        std::cin >> worth;
        // interesting bug, sign of -n%2 is undefined behaviour, can be -ve, so don't
        // do worth%2 == 1.
        if(worth%2 == 0) {
            pos_alex[i] = false;
            books_B.push_back(worth);
        } else {
            pos_alex[i] = true;
            books_A.push_back(worth);
        }
    }
    return pos_alex;
}

std::vector<int> solve(std::vector<bool>& pos_alex, std::vector<int>& books_A, std::vector<int>& books_B) {
    int sz = pos_alex.size();
    // A increasing order.
    std::sort(books_A.begin(), books_A.end());
    // B decreasing order.
    std::sort(books_B.rbegin(), books_B.rend());
    std::vector<int> res(sz);
    int i_A = 0, i_B = 0;
    for(int i=0; i<sz; i++) {
        if(pos_alex[i]) {
            res[i] = books_A[i_A];
            i_A++;
        } else {
            res[i] = books_B[i_B];
            i_B++;
        }
    }
    return res;
}

int main() {
    int ncases;
    std::cin >> ncases;
    for(int i=1; i<=ncases; i++) {
        std::vector<int> books_A, books_B;
        std::vector<bool> pos_alex = read_input(books_A, books_B);
        std::vector<int> res = solve(pos_alex, books_A, books_B);
        std::cout << "Case #" << i << ": ";
        for(int i=0; i<res.size()-1; i++) {
            std::cout << res[i] << " ";
        }
        std::cout << res[res.size()-1] << std::endl;
    }
}