# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-v/

def maximumProfit(prices: list[int], k: int) -> int:
    mp = [[-float('inf')] * 3 for _ in range(k + 1)]

    for i in range(k + 1):
        mp[i][0] = 0
        
    for i in prices:
        tmp = [[-float('inf')] * 3 for _ in range(k + 1)]

        for j in range(k + 1):
            tmp[j][0] = max(tmp[j][0], mp[j][0])

            if j > 0:
                tmp[j - 1][1] = max(tmp[j - 1][1], mp[j][0] - i)
                tmp[j - 1][2] = max(tmp[j - 1][2], mp[j][0] + i)

            tmp[j][1] = max(tmp[j][1], mp[j][1])
            tmp[j][0] = max(tmp[j][0], mp[j][1] + i)
            
            tmp[j][2] = max(tmp[j][2], mp[j][2])
            tmp[j][0] = max(tmp[j][0], mp[j][2] - i)

        mp = tmp
        
    return max(i[0] for i in mp) # (3527 ms)