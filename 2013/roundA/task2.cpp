#include <iostream>
#include <string>
#include <map>

// get numbers of any no of digits and a format i1-i2-...-in
// can get up to a 100 digit number, so unrealistic to store as even a long int.
// read input as a string seperated into the correct format by single spaces.

// I'm using the wrong language here, so its no wonder writting the code is a nightmare.

std::map<int, std::string> dig_names {
    {0, "zero"},
    {1, "one"},
    {2, "two"},
    {3, "three"},
    {4, "four"},
    {5, "five"},
    {6, "six"},
    {7, "seven"},
    {8, "eight"},
    {9, "nine"}
};

std::map<int, std::string> mult {
    {2, "double"},
    {3, "triple"},
    {4, "quadruple"},
    {5, "quintuple"},
    {6, "sextuple"},
    {7, "septuple"},
    {8, "octuple"},
    {9, "nonuple"},
    {10, "decuple"}
};

std::string solve() {
    std::string num, fmt;
    std::cin >> num >> fmt;
    std::string res;
    int i_num = 0;
    for(int i=0; i<fmt.size(); i++) {
        if(fmt[i] == '-') break;
        // assume a standard encoding so that '0', '1', ... '9' are contiguous.
        int ndig = fmt[i] - '0';
        int last_dig = -1, cur_dig = -2, nrep = 1;
        // for the last digit we also want to trigger a print.
        for(int j=0; j<ndig; j++) {
            cur_dig = num[i_num] - '0';
            if((cur_dig == last_dig) && (j != ndig-1)) {
                nrep++;
            } else {
                if(1 < nrep && nrep <= 10) {
                    res += (mult[nrep] + dig_names[cur_dig]); 
                } else {
                    for(int k=0; k<nrep; k++) {
                        res += dig_names[cur_dig];
                    }
                }
                nrep = 1;
            }
            last_dig = cur_dig;
            i_num++;
        }
    }
    return res;
}

int main() {
    int ncases;
    std::cin >> ncases;
    for(int i=1; i<=ncases; i++) {
        std::string res = solve();
        std::cout << "Case #" << i << ": " << res << std::endl;
    }
}