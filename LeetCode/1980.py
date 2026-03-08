# https://leetcode.com/problems/find-unique-binary-string/

def findDifferentBinaryString(nums: list[str]) -> str:
    a = []

    for i in range(len(nums)):
        a.append('1' if nums[i][i] == '0' else '0')
        
    return "".join(a) # (0 ms)