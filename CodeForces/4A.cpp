// https://codeforces.com/problemset/problem/4/A

#include <iostream>

int main() {
    int w;
    std::cin >> w;

    // The weight must be event and greater than 2
    if (w > 2 && w % 2 == 0) {
        std::cout << "YES" << std::endl;
    } else {
        std::cout << "NO" << std::endl;
    }

    return 0; // T: O(1)
}
