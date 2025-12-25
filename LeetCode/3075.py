# https://leetcode.com/problems/maximize-happiness-of-selected-children/

def maximumHappinessSum(happiness: list[int], k: int) -> int:
    happiness.sort(reverse=True)
    
    t = 0
    
    for i in range(k):
        t += (max(0, happiness[i] - i))
    
    return t # (824 ms)