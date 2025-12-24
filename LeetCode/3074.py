# https://leetcode.com/problems/apple-redistribution-into-boxes/description/?envType=daily-question&envId=2025-12-24

def minimumBoxes(apple: list[int], capacity: list[int]) -> int:
    t, b = sum(apple), 0

    capacity.sort(reverse=True)

    for i in capacity:
        t -= i
        b += 1

        if t <= 0: return b
            
    return b # (0 ms)