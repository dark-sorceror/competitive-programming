// https://codeforces.com/problemset/problem/2290/A

#include <iostream>

int main() {
    std::ios::sync_with_stdio(false);
    std::cin.tie(nullptr);

    int t;
    std::cin >> t;

    while (t--) {
        int a, b, c;
        std::cin >> a >> b >> c;

        if (a + 1 == b && b + 1 == c) {
            std::cout << "YES\n";
        } else {
            std::cout << "NO\n";
        }
    }

    return 0; // T: O(n)
}