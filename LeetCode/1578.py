# https://leetcode.com/problems/minimum-time-to-make-rope-colorful/

def minCost(colors: str, neededTime: list[int]) -> int:
    p, c, s = "", "", 0

    for i in range(len(list(colors))):
        c = colors[i]

        if c == p:
            if neededTime[i] > neededTime[i - 1]:
                s += neededTime[i - 1]
            else:
                s += neededTime[i]
                
        p = c
    
    return s