// https://codeforces.com/problemset/problem/2278/D

#include <algorithm>
#include <iostream>
#include <vector>

int main() {
    std::ios::sync_with_stdio(false);
    std::cin.tie(nullptr);

    int c;
    std::cin >> c;

    while (c--) {
        int n;
        std::cin >> n;

        std::vector<long long> a(n);

        for (int i = 0; i < n; i++) {
            std::cin >> a[i];
        }

        // We can lock non-adjacents, so sorting from least to greatest
        // makes the array more organized. Order doesn't matter since
        // adding to the unlocked elements raises everything except the
        // locked element(s)
        std::sort(a.begin(), a.end());

        long long totalCost = 0;

        for (int i = 1; i < n; i++) {
            // i represents the number immediately after the gap

            // The gap represents the difference between the numbers
            long long gap = a[i] - a[i - 1];

            // Greedy choice: The amount of elements that are locked will be
            // the side with the least amount of elements to minimize cost.
            // Moving the other side toward it closes this gap without
            // changing the gaps within either side.
            int locked = std::min(i, n - i);

            // Closing the gap costs the size of the gap x the
            // number of locked elements
            totalCost += gap * locked;
        }

        // Number of operations is just the sum of the gaps,
        // which is also the difference between the highest
        // element and the lowest element (already sorted)
        long long operations = a[n - 1] - a[0];

        std::cout << totalCost << " " << operations << std::endl;
    }

    return 0; // T: O(n log n)
}
