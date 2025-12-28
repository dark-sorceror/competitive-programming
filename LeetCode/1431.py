# https://leetcode.com/problems/kids-with-the-greatest-number-of-candies/

def kidsWithCandies(candies: list[int], extraCandies: int) -> list[bool]:
    m = max(candies)

    return [i + extraCandies >= m for i in candies] # (0 ms)