# https://leetcode.com/problems/minimum-distance-to-type-a-word-using-two-fingers/

def minimumDistance(word: str) -> int:
    def get_dist(a, b):
        if a == 26: return 0
        
        x1, y1 = divmod(a, 6)
        x2, y2 = divmod(b, 6)

        return abs(x1 - x2) + abs(y1 - y2)

    a = [ord(c) - ord('A') for c in word]
    
    dp = [0] * 27
    
    for i in range(len(word) - 1):
        c, nxt = a[i], a[i + 1]
        new_dp = [float('inf')] * 27
        
        for other in range(27):
            if dp[other] == float('inf'): continue
            
            new_dp[other] = min(new_dp[other], dp[other] + get_dist(c, nxt))
            
            new_dp[c] = min(new_dp[c], dp[other] + get_dist(other, nxt))
            
        dp = new_dp
        
    return min(dp) # (83 ms)