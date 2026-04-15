# https://leetcode.com/problems/minimum-total-distance-traveled/

def minimumTotalDistance(robot: list[int], factory: list[list[int]]) -> int:
    robot.sort()
    factory.sort()
    
    n, m = len(robot), len(factory)
    
    # Min distance for first i factories to repair first j robots
    dp = [[float('inf')] * (n + 1) for _ in range(m + 1)]
    dp[0][0] = 0
    
    for i in range(1, m + 1):
        p, l = factory[i - 1]

        for j in range(n + 1):
            # Repairs 0 robots
            dp[i][j] = dp[i - 1][j]
            
            # Repairs 'k' robots
            c = 0
            for k in range(1, min(j, l) + 1):
                c += abs(robot[j - k] - p)

                if dp[i - 1][j - k] != float('inf'):
                    dp[i][j] = min(dp[i][j], dp[i - 1][j - k] + c)
                    
    return dp[m][n] # (902 ms)