# https://leetcode.com/problems/find-smallest-letter-greater-than-target/

def nextGreatestLetter(letters: list[str], target: str) -> str:
    l, r = 0, len(letters) - 1
    
    if target >= letters[-1]:
        return letters[0]
    
    while l <= r:
        m = l + (r - l) // 2

        if letters[m] <= target: l = m + 1
        else: r = m - 1
    
    return letters[l] # (0 ms)