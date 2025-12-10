#include <iostream>
#include <vector>
#include <unordered_set>

using namespace std;

int countPermutations(vector<int> &complexity)
{
    long long t = 1;
    int n = complexity.size();
    vector<unordered_set<int>> p(n);

    for (int i = 1; i < n; ++i)
    {
        for (int j = 0; j < i; ++j)
        {
            if (complexity[j] < complexity[i])
            {
                p[i].insert(j);
            }
        }

        if (p[i].empty())
        {
            return 0;
        }
    }

    unordered_set<int> u;
    u.insert(0);
    unordered_set<int> r;

    for (int i = 1; i < n; i++)
    {
        if (p[i].count(0) && p[i].size() == 1)
        {
            r.insert(i);
        }
    }

    r.clear();

    for (int i = 1; i < n; i++)
    {
        if (p[i].count(0))
        {
            r.insert(i);
        }
    }

    for (int i = 1; i < n; ++i)
    {
        long long c = r.size();

        if (!c)
        {
            return 0;
        }

        t = (t * c) % (1000000007);

        int k = *r.begin();
        r.erase(k);
        u.insert(k);
    }

    return t;
}