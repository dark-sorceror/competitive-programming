# https://leetcode.com/problems/can-place-flowers/

def canPlaceFlowers(flowerbed: list[int], n: int) -> bool:
    if n == 0: return True

    flowerbed = [0] + flowerbed + [0]

    for i in range(len(flowerbed) - 2):
        l, r = i, i + 2

        if flowerbed[l] == flowerbed[r] == 0 and not flowerbed[i + 1]:
            n -= 1
            flowerbed[i + 1] = 1

            if n == 0: return True
    
    return False # (3 ms)