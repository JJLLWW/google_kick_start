#include <iostream>
#include <vector>
#include <cstdint>
#include <numeric>

// large binary tree, root 1/1.
// at node p/q, left child is p/(p+q), right child is (p+q)/q
// 2 questions: 
// 1) find the nth element (counting from 1) of a level-order traversal of the tree.
// 2) given p/q find its position in a level order traversal of the tree.

// 64 bit numbers sufficient uint64, however can get so large a brute force method wont work.

// 1) Levels (1), (2, 3), (4, 5, 6, 7)
// size of level l (counting from 1) is 2^(l-1), level of n is ceil(log_2(n))+1, consists of integers
// in range [2^(l-1), 2^l). can get a relative index i from n - 2^(l-1).

// 2) if have p/q, parent is p'/q' then:
// either> p/q = p'/(p'+q') and q' = q - p, so p' = p. (L)
// or> p/q = (p'+q')/q' and p' = p - q so q' = q. (R)
// if know sequence of moves LRRL..LR to get to p/q, p/q is at position n where n is LRRL...LR in binary
// (L=0, R=1)

// cpp has no built in fraction support, should I be doing this in python?

// BUGGED
void get_nth_elem(std::uint64_t n, std::uint64_t& p, std::uint64_t& q) {
    // index levels of the tree from 0. Get the level of p/q.
    int level = 0;
    std::uint64_t two_pow_l = 1;
    while(true) {
        if(two_pow_l*2 > n) break;
        level++;
        two_pow_l *= 2;
    }
    // the index (from 0) of p/q on its level.
    std::uint64_t i = n - two_pow_l;
    p = 1, q = 1;
    two_pow_l /= 2;
    while(two_pow_l != 0) {
        std::uint64_t p_old = p, q_old = q;
        // go along left branch
        if(i/two_pow_l == 0) {
            p = p_old;
            q = p_old + q_old;
        }
        // go along right branch
        else {
            p = p_old + q_old;
            q = q_old;
        }
        // may not be in lowest terms.
        std::uint64_t d = std::gcd(p, q);
        p /= d;
        q /= d;
        two_pow_l /= 2;
    }
}

// can get string of left and right moves in reverse order, need to actually get the index.
std::uint64_t get_pq_idx(std::uint64_t p, std::uint64_t q) {
    // the left and right moves are the binary digits of n, get in reverse order.
    std::vector<unsigned int> bin_dig_rev;
    while((p != 1) || (q != 1)) {
        // may not be in lowest terms.
        std::uint64_t d = std::gcd(p, q);
        p /= d;
        q /= d;
        std::uint64_t p_old = p, q_old = q;
        // left
        if(p < q) {
            q = q_old - p_old;
            p = p_old;
            bin_dig_rev.push_back(0);
        } 
        // right
        else if(q < p) {
            p = p_old - q_old;
            q = q_old;
            bin_dig_rev.push_back(1);
        }
    }
    // "leading" 1
    bin_dig_rev.push_back(1);
    std::uint64_t pow2 = 1 , res = 0;
    for(unsigned int dig : bin_dig_rev) {
        res += dig*pow2;
        pow2 *= 2;
    }
    return res;
}

int main() {
    int ncases;
    std::cin >> ncases;
    for(int i=1; i<=ncases; i++) {
        std::uint64_t id, n, p, q;
        std::cin >> id;
        if(id == 2) {
            std::cin >> p >> q;
            n = get_pq_idx(p, q);
            std::cout << "Case #" << i << ": " << n << std::endl;
        } else {
            std::cin >> n;
            get_nth_elem(n, p, q);
            std::cout << "Case #" << i << ": " << p << " " << q << std::endl;
        }
    }
}