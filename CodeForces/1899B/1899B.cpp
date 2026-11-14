// https://codeforces.com/problemset/problem/1899/B

#include <algorithm>
#include <iostream>
#include <limits>
#include <vector>

int main() {
    std::ios::sync_with_stdio(false);
    std::cin.tie(nullptr);

    int t;
    std::cin >> t;

    while (t--) {
        int n;
        std::cin >> n;

        // prefix[i] = sum of the first i elements
        std::vector<long long> prefix(n + 1, 0);

        for (int i = 0; i < n; i++) {
            long long value;
            std::cin >> value;

            prefix[i + 1] = prefix[i] + value;
        }

        long long answer = 0;

        for (int k = 1; k <= n; k++) {
            // Every group must contain exactly k elements
            if (n % k != 0) {
                continue;
            }

            long long smallest = std::numeric_limits<long long>::max();
            long long largest = 0;

            for (int right = k; right <= n; right += k) {
                long long groupSum = prefix[right] - prefix[right - k];

                smallest = std::min(smallest, groupSum);
                largest = std::max(largest, groupSum);
            }

            answer = std::max(answer, largest - smallest);
        }

        std::cout << answer << std::endl;
    }

    return 0; // T: O(n log n)
}