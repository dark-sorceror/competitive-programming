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

    int minimumHeight = 1000000;
    int bestStart = 0;

    for (int i = 1; i <= n - k + 1; i++) {
        int windowSum = 0;

        for (int j = 0; j < k; j++) {
            windowSum += heights[j + i - 1];
        }

        if (windowSum < minimumHeight) {
            minimumHeight = windowSum;
            bestStart = i;
        }
    }

    std::cout << bestStart << std::endl;

    return 0; // T: O(n * k)
}