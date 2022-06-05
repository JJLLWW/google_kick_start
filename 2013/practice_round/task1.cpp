#include <iostream>
#include <string>
#include <vector>
#include <algorithm>

// order, space then upper case chars then lower case chars.

// want L[0] <= L[1] <= L[2] <= ... <= L[N-1], (< lexicographically less.)
// algorithm: go through pairs (L[i], L[i+1]), if L[i+1] < L[i] put L[i] in the correct
// place in the left hand list. (1 operation)

// RVO
std::vector<std::string> read_input() {
    int N;
    std::cin >> N;
    std::cin.ignore();
    std::vector<std::string> cards(N);
    for(int i=0; i<N; i++) {
        std::getline(std::cin, cards[i]);
    }
    return cards;
}

// instead of going through the algorithm just place the "maximum value" at L[i].
int solve(std::vector<std::string>& cards) {
    int N = cards.size();
    if(N == 1) { 
        return 0;
    }
    int nmoves = 0;
    std::vector<std::string>::iterator cur_it;
    // std::max_element.
    for(int i=0; i<N-1; i++) {
        if(cards[i+1] < cards[i]) {
            cur_it = cards.begin();
            std::advance(cur_it, i+1);
            std::string max = *std::max_element(cards.begin(), cur_it);
            cards[i+1] = max;
            nmoves++;
        }
    }
    return nmoves;
}

int main() {
    int ncases;
    std::cin >> ncases;
    for(int i=1; i<=ncases; i++) {
        std::vector<std::string> cards = read_input();
        int nmoves = solve(cards);
        std::cout << "Case #" << i << ": " << nmoves << std::endl;
    }
}