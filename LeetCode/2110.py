# https://leetcode.com/problems/number-of-smooth-descent-periods-of-a-stock/

def getDescentPeriods(prices: list[int]) -> int:
    n = len(prices)

    c, t = 1, 1

    for i in range(1, n):
        if prices[i] == prices[i - 1] - 1: c += 1
        else: c = 1

        t += c
        
    return t # (51 ms)