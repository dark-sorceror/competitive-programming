# https://leetcode.com/problems/binary-prefix-divisible-by-5/

def prefixesDivBy5(nums: list[int]) -> list[bool]:
    answer, r = [], 0

    for i in nums:
        r = (r * 2 + i) % 5

        answer.append(r == 0)
        
    return answer # (0 ms)