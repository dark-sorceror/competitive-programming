# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-using-strategy/

def maxProfit(prices: list[int], strategy: list[int], k: int) -> int:
    n = len(prices)
    p = sum(p * s for p, s in zip(prices, strategy))

    cs, os = 0, 0

    for i in range(k):
        os += strategy[i] * prices[i]

    for i in range(k // 2, k):
        cs += prices[i]

    md = cs - os

    for i in range(1, n - k + 1):
        l, r = i + k - 1, i - 1

        os -= strategy[r] * prices[r]
        os += strategy[l] * prices[l]

        nr, nl = i - 1 + (k // 2), i + k - 1
        
        cs -= prices[nr]
        cs += prices[nl]

        d = cs - os

        if d > md: md = d

    return p + max(0, md) # (211 ms)