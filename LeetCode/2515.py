# https://leetcode.com/problems/shortest-distance-to-target-string-in-a-circular-array/

def closestTarget(words: list[str], target: str, startIndex: int) -> int:
    n = len(words)
    m = n
    f = False

    for i in range(n):
        if words[i] == target:
            f = True

            m = min(m, abs(i - startIndex), n - abs(i - startIndex))
            
    return m if f else -1 # (0 ms)