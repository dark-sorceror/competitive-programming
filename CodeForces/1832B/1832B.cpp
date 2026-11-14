#include <algorithm>
#include <iostream>
#include <vector>

int main() {
    std::ios::sync_with_stdio(false);
    std::cin.tie(nullptr);

    int t;
    std::cin >> t;

    while (t--) {
        int n, k;
        std::cin >> n >> k;

        std::vector<long long> a(n);

        for (long long &value : a) {
            std::cin >> value;
        }

        std::sort(a.begin(), a.end());

        // prefix[i] = sum of the first i elements
        std::vector<long long> prefix(n + 1, 0);

        for (int i = 0; i < n; i++) {
            prefix[i + 1] = prefix[i] + a[i];
        }

        long long answer = 0;

        // x operations remove two minimums each. The remaining
        // k - x operations remove one maximum each
        for (int x = 0; x <= k; x++) {
            int left = 2 * x;
            int right = n - (k - x);

            long long remainingSum = prefix[right] - prefix[left];

            answer = std::max(answer, remainingSum);
        }

        std::cout << answer << std::endl;
    }

    return 0; // T: O(n log n)
}