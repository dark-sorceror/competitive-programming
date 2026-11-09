// https://codeforces.com/problemset/problem/110/A

#include <iostream>
#include <string>

int main() {
    std::ios::sync_with_stdio(false);
    std::cin.tie(nullptr);

    std::string s;
    std::cin >> s;

    int count = 0;

    for (char ch : s) {
        if (ch == '4' || ch == '7') {
            count++;
        }
    }

    if (count == 4 || count == 7) {
        std::cout << "YES" << std::endl;
    } else {
        std::cout << "NO" << std::endl;
    }

    return 0; // T: O(n)
}