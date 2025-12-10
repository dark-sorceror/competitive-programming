// https://leetcode.com/problems/count-the-number-of-computer-unlocking-permutations/

#include <iostream>
#include <vector>

using namespace std;

int countPermutations(vector<int> &complexity)
{
    long long t = 1;
    int n = complexity.size();

    for (int i = 1; i < n; i++)
    {
        if (complexity[i] <= complexity[0])
        {
            return 0;
        }
    }

    for (int i = 1; i < n; i++)
    {
        t = (t * i) % (1000000007);
    }

    return t; // (0 ms)
}