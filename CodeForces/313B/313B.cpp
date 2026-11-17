// https://codeforces.com/problemset/problem/313/B

#include <iostream>
#include <string>
#include <vector>

int main() {
    std::ios::sync_with_stdio(false);
    std::cin.tie(nullptr);

    std::string s;
    std::cin >> s;

    int n = static_cast<int>(s.size());

    // prefix[i] counts equal adjacent pairs in the first i characters
    std::vector<int> prefix(n + 1, 0);

    for (int i = 1; i < n; i++) {
        prefix[i + 1] = prefix[i] + (s[i] == s[i - 1]);
    }

    int m;
    std::cin >> m;

    while (m--) {
        int l, r;
        std::cin >> l >> r;

        std::cout << prefix[r] - prefix[l] << '\n';
    }

    return 0; // T: O(n + m)
}