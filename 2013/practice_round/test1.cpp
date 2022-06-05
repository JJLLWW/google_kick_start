// does c++ string lexicographical ordering behave how we need it to?

#include <iostream>
#include <string>

int main() {
    int count = 0;
    std::string str1, str2;
    while(true) {
        if(count%2 == 0) {
            std::cout << "string 1> ";
            std::getline(std::cin, str1);
        }
        else {
            std::cout << "string 2> ";
            std::getline(std::cin, str2);
            if(str1 < str2) {
                std::cout << "string 1 was lexicographically less than string 2" << std::endl;
            } else {
                std::cout << "string 1 was not lexicographically less than string 2" << std::endl;
            }
        }
        count++;
    }
}