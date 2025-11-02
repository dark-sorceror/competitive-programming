# https://leetcode.com/problems/the-two-sneaky-numbers-of-digitville/

def getSneakyNumbers(nums: list[int]) -> list[int]:
    # Method 1: Find when count(i) > 1
    
    """
    sn = []
    
    for i in range(len(nums)):
        if nums.count(i) > 1:
            sn.append(i)
    
    return sn
    
    """ # (15 ms)
    
    # return list(set(i for i in nums if nums.count(i) > 1)) Too slow... (3 ms)
    
    # ---
    
    # Method 2: Compare with a running set
    
    u = set()
    
    return [i for i in nums if i in u or u.add(i)] # (0 ms)