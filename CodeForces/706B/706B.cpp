// https://codeforces.com/problemset/problem/706/B

#include <algorithm>
#include <iostream>
#include <vector>

int main() {
    std::ios::sync_with_stdio(false);
    std::cin.tie(nullptr);

    int n;
    std::cin >> n;

    std::vector<int> prices(n);

    for (int &price : prices) {
        std::cin >> price;
    }

    std::sort(prices.begin(), prices.end());

    int q;
    std::cin >> q;

    while (q--) {
        int budget;
        std::cin >> budget;

        auto it = std::upper_bound(prices.begin(), prices.end(), budget);
        int affordable = static_cast<int>(it - prices.begin());

        std::cout << affordable << '\n';
    }

    return 0; // T: O(n log n + q log n)
}