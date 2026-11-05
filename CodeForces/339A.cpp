// https://codeforces.com/problemset/problem/339/A

#include <algorithm>
#include <iostream>
#include <string>

int main() {
    std::ios::sync_with_stdio(false);
    std::cin.tie(nullptr);

    std::string s;
    std::cin >> s;

    std::string numbers;

    for (char ch : s) {
        if (ch != '+') {
            numbers += ch;
        }
    }

    std::sort(numbers.begin(), numbers.end());

    for (std::size_t i = 0; i < numbers.size(); i++) {
        std::cout << numbers[i];

        if (i != numbers.size() - 1) {
            std::cout << "+";
        }
    }

    std::cout << std::endl;

    return 0; // T: O(n log n)
}