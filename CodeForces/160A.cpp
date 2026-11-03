// https://codeforces.com/problemset/problem/160/A

#include <algorithm>
#include <iostream>
#include <numeric>
#include <vector>

int main() {
    std::ios::sync_with_stdio(false);
    std::cin.tie(nullptr);

    int n;
    std::cin >> n;

    std::vector<int> coins(n);

    for (int &coin : coins) {
        std::cin >> coin;
    }

    // Sort from highest to lowest, the greedy choice
    // is to start from the highest valued coins
    std::sort(coins.rbegin(), coins.rend());

    int coinsTaken = 0;
    int valueTaken = 0;
    int totalValue = std::accumulate(coins.begin(), coins.end(), 0);

    for (int coin : coins) {
        valueTaken += coin;
        coinsTaken++;

        if (coinsTaken > totalValue - valueTaken) {
            break;
        }
    }

    std::cout << coinsTaken << std::endl;

    return 0; // T: O(n log n)
}