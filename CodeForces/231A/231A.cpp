// https://codeforces.com/problemset/problem/231/A

#include <iostream>

int main() {
    std::ios::sync_with_stdio(false);
    std::cin.tie(nullptr);

    int n;
    std::cin >> n;

    int problems = 0;

    for (int i = 0; i < n; i++) {
        int p, v, t;
        std::cin >> p >> v >> t;

        if (p + v + t >= 2) {
            problems++;
        }
    }

    std::cout << problems << std::endl;

    return 0; // T: O(n)
}