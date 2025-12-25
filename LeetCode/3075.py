# https://leetcode.com/problems/maximize-happiness-of-selected-children/

def maximumHappinessSum(happiness: list[int], k: int) -> int:
    t = 0
    
    for i in range(k):
        h = happiness.pop(happiness.index(max(happiness)))
        t += (max(0, h - (1 * i)))
    
    return t