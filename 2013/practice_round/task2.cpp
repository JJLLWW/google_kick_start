#include <iostream>
#include <cmath>

// g = 9.8, no air res
// particle at O moves at speed V, angle theta from horizontal, and lands horizontal dist D away from O.
// get theta in degrees.

// From algebra + trig:
// (-0.5*g*D^2/V^2)*tan^2(th) + D*tan(th) + (-0.5*g*D^2/V^2) = 0.

constexpr double PI = 3.14159265358979323846;

void read_input(int& V, int& D) {
    std::cin >> V >> D;
}

double solve(int V, int D) {
    double th, th_rad, tan_th;
    double g = 9.8;
    double A, B, C;
    A = -g*D*D/(2*V*V), B = D, C = A;
    double disc = B*B - 4*A*C;
    // may get disc < 0 through floating point precision errors, just correct as can
    // assume all cases soluble.
    if(disc < 0) 
        disc = 0;
    tan_th = (-B + std::sqrt(disc))/(2*A);
    th_rad = std::atan(tan_th);
    th = 360*th_rad/(2*PI);
    return th;
}

int main() {
    int ncases;
    std::cin >> ncases;
    // iostream ugh, precision is number of digits after the decimal point.
    std::cout.precision(15);
    for(int i=1; i<=ncases; i++) {
        // I'm assuming V and D are always integers.
        int V, D;
        read_input(V, D);
        double th = solve(V, D);
        std::cout << "Case #" << i << ": " << th << std::endl;
    }
}