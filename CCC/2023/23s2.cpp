#include "bits/stdc++.h"
#define int long long

using namespace std;

const int MAX = 5008;
int heights[MAX], mountains[MAX][MAX];

int32_t main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int N;
    cin >> N;

    for (int i = 0; i <= (N - 1); i++) {
        int x;
        cin >> x;

        heights[i] = x;
    }

    for (int i = 0; i <= (N - 1); i++) {
        int left = 0, right = i, best = 1e18;

        while (right <= (N - 1)) {
            mountains[left][right] = abs(heights[left] - heights[right]) + mountains[left + 1][right - 1];
        
            best = min(best, mountains[left][right]);

            left++, right++;
        }
        cout << best;
        if (i != (N - 1)) cout << " ";
    }


}