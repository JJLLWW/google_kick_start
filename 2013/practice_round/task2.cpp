#include <iostream>
// better way?
#include <cmath>

// g = 9.8, no air res
// particle at O moves at speed V, angle theta from horizontal, and lands horizontal dist D away from O.
// get theta in degrees.

// tan^2 + 1 = sec^2
// V*cos(th)*T = D -> T = D/(V*sin(th)).
// 0 = -0.5*g*T^2 + V*sin(th)*T -> 0 = (-0.5*g*D^2/V^2)*sec^2(th) + V*tan(th).
// (-0.5*g*D^2/V^2)*tan^2(th) + V*tan(th) + (-0.5*g*D^2/V^2) = 0.

constexpr double PI = 3.14159265358979323846;

void read_input(int& V, int& D) {
    std::cin >> V >> D;
}

double solve(int V, int D) {
    double th, th_rad;
    double g = 9.8;
    double A, B, C;
    A = -0.5*g*D*D/(V*V), B = V, C = A;
    th_rad = std::atan((B + std::sqrt(B*B - 4*A*C))/(2*A));
    th = 2*PI*th_rad/360;
    return th;
}

int main() {
    int ncases;
    std::cin >> ncases;
    for(int i=1; i<=ncases; i++) {
        // I'm assuming V and D are always integers.
        int V, D;
        read_input(V, D);
        double th = solve(V, D);
        std::cout << "Case #" << i << ": " << th << std::endl;
    }
}