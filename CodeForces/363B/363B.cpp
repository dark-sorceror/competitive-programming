// https://codeforces.com/problemset/problem/363/B

#include <iostream>
#include <vector>

int main() {
    std::ios::sync_with_stdio(false);
    std::cin.tie(nullptr);

    int n, k;
    std::cin >> n >> k;

    std::vector<int> heights(n);

    for (int &i : heights) {
        std::cin >> i;
    }

    int windowSum = 0;

    for (int i = 0; i < k; i++) {
        windowSum += heights[i];
    }

    int minimumHeight = windowSum;
    int bestStart = 1;

    for (int i = 1; i <= n - k; i++) {
        windowSum -= heights[i - 1];
        windowSum += heights[i + k - 1];

        if (windowSum < minimumHeight) {
            minimumHeight = windowSum;
            bestStart = i + 1;
        }
    }

    std::cout << bestStart << std::endl;

    return 0; // T: O(n)
}