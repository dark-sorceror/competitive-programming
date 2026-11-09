// https://codeforces.com/problemset/problem/50/A

#include <iostream>

int main() {
    std::ios::sync_with_stdio(false);
    std::cin.tie(nullptr);

    int M, N;

    std::cin >> M >> N;
    std::cout << (M * N) / 2 << std::endl;

    return 0; // T: O(1)
}