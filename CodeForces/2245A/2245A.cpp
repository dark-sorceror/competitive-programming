// https://codeforces.com/problemset/problem/2245/A

#include <iostream>
#include <string>

int main() {
    std::ios::sync_with_stdio(false);
    std::cin.tie(nullptr);

    int c;
    std::cin >> c;

    while (c--) {
        int n, k;
        std::string s;
        std::cin >> n >> k >> s;

        // Case where the flipping the middle does not
        // satisfy the requirement on either side
        if (2 * k > n) {
            std::cout << -1 << std::endl;
        } else {
            int flips = 0;

            // Since all pigges need to satisfy the requirement
            // the focus is on the edge piggies since they are the
            // easiest to fail the requirement. The greedy observation
            // is that the ends must be k R's or L's and the middle can
            // be ignored to minimize flips

            // First k pigges must face right
            for (int i = 0; i < k; i++) {
                // Following that greedy approach, this position
                // must be R, so flip it if it isn't
                if (s[i] == 'L') {
                    flips++;
                }
            }

            // Last k pigges must face left
            for (int i = n - k; i < n; i++) {
                if (s[i] == 'R') {
                    flips++;
                }
            }

            std::cout << flips << std::endl;
        }
    }

    return 0; // T: O(n)
}