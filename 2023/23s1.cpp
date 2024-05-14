#include "bits/stdc++.h"
#define int long long

using namespace std;

int32_t main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int C, output = 0;
    cin >> C;

    int triangles[2][C];

    for (int i = 0; i <= 1; i++) {
        for (int j = 0; j <= C - 1; j++) {
            int x;
            cin >> x;
            triangles[i][j] = x;
        }
    }

    for (int i = 0; i <= 1; i++) {
        for (int j = 0; j <= C - 1; j++) {
            if (triangles[i][j] == 1) {
                int sides = 3;

                if (j != 0) {
                    if (triangles[i][j - 1] == 1) {
                        sides--;
                    }
                }

                if (j != C - 1) {
                    if (triangles[i][j + 1] == 1) {
                        sides--;
                    }
                }

                if (j % 2 != 1 && i == 1) {
                    if (triangles[0][j] == 1) {
                        sides -= 2;
                    }
                }

                output += sides;
            }
        }
    }

    cout << output;
}