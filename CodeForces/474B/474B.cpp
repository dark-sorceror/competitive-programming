// https://codeforces.com/problemset/problem/474/B

#include <algorithm>
#include <iostream>
#include <vector>

int main() {
    std::ios::sync_with_stdio(false);
    std::cin.tie(nullptr);

    int n;
    std::cin >> n;

    // prefix[i] = total worms in the first i piles
    std::vector<int> prefix(n + 1, 0);

    for (int i = 1; i <= n; i++) {
        int worms;
        std::cin >> worms;

        prefix[i] = prefix[i - 1] + worms;
    }

    int m;
    std::cin >> m;

    while (m--) {
        int q;
        std::cin >> q;

        auto it = std::lower_bound(prefix.begin() + 1, prefix.end(), q);
        int pile = static_cast<int>(it - prefix.begin());

        std::cout << pile << '\n';
    }

    return 0; // T: O(n + m log n)
}