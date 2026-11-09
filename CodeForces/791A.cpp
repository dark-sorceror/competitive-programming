// https://codeforces.com/problemset/problem/791/A

#include <iostream>

int main() {
    std::ios::sync_with_stdio(false);
    std::cin.tie(nullptr);

    int a, b;
    std::cin >> a >> b;

    int years = 0;

    while (a <= b) {
        a *= 3;
        b *= 2;
        years++;
    }

    std::cout << years << std::endl;

    return 0; // T: O(1):
}