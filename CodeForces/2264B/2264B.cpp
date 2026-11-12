// https://codeforces.com/problemset/problem/2264/B

#include <algorithm>
#include <iostream>
#include <limits>
#include <queue>

int main() {
    std::ios::sync_with_stdio(false);
    std::cin.tie(nullptr);

    int t;
    std::cin >> t;

    while (t--) {
        int n, m;
        std::cin >> n >> m;

        // The score telescopes to m * b[m] - (b[1] + ... + b[m - 1]).
        // For a fixed last element, choose the m - 1 smallest earlier values
        std::priority_queue<int> smallest;
        long long sum = 0;
        long long answer = std::numeric_limits<long long>::lowest();

        for (int i = 0; i < n; i++) {
            int value;
            std::cin >> value;

            // Evaluate before inserting: the last element cannot also be
            // one of the earlier chosen elements
            if (i >= m - 1) {
                answer = std::max(answer, 1LL * m * value - sum);
            }

            smallest.push(value);
            sum += value;

            // Remove the largest to retain only the m-1 smallest values
            if (static_cast<int>(smallest.size()) > m - 1) {
                sum -= smallest.top();
                smallest.pop();
            }
        }

        std::cout << answer << '\n';
    }

    return 0; // T: O(n log(m + 1))
}
