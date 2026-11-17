// https://codeforces.com/problemset/problem/433/B

#include <algorithm>
#include <iostream>
#include <vector>

int main() {
    std::ios::sync_with_stdio(false);
    std::cin.tie(nullptr);

    int n;
    std::cin >> n;

    std::vector<long long> a(n);

    for (long long &value : a) {
        std::cin >> value;
    }

    // Prefix sums in the original order
    std::vector<long long> originalPrefix(n + 1, 0);

    for (int i = 0; i < n; i++) {
        originalPrefix[i + 1] = originalPrefix[i] + a[i];
    }

    std::sort(a.begin(), a.end());

    // Prefix sums in sorted order
    std::vector<long long> sortedPrefix(n + 1, 0);

    for (int i = 0; i < n; i++) {
        sortedPrefix[i + 1] = sortedPrefix[i] + a[i];
    }

    int m;
    std::cin >> m;

    while (m--) {
        int type, l, r;
        std::cin >> type >> l >> r;

        if (type == 1) {
            std::cout << originalPrefix[r] - originalPrefix[l - 1] << std::endl;
        } else {
            std::cout << sortedPrefix[r] - sortedPrefix[l - 1] << std::endl;
        }
    }

    return 0; // T: O(n log n + m)
}