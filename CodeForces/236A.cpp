// https://codeforces.com/problemset/problem/236/A

#include <iostream>
#include <string>
#include <unordered_map>

int main() {
    std::ios::sync_with_stdio(false);
    std::cin.tie(nullptr);

    std::string s;
    std::cin >> s;

    // First, filter out the duplicates
    std::unordered_map<char, int> frequency;

    for (char ch : s) {
        frequency[ch]++;
    }

    if (frequency.size() % 2 == 0) {
        std::cout << "CHAT WITH HER!" << std::endl;
    } else {
        std::cout << "IGNORE HIM!" << std::endl;
    }

    return 0; // T: O(n)
}