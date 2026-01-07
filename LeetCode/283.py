def moveZeroes(nums: list[int]) -> None:
    l, r = 0, 1

    while r < len(nums):
        if nums[l] == 0 and nums[r]:
            nums[l], nums[r] = nums[r], nums[l]
            
            l += 1
            r += 1
        elif nums[r] == nums[l] == 0:
            r += 1
        else:
            l += 1
            r += 1
    
    return nums # (7 ms)