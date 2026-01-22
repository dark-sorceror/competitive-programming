# https://leetcode.com/problems/minimum-pair-removal-to-sort-array-i/

def minimumPairRemoval(nums: list[int]) -> int:
    o = 0

    while True:
        s = True

        for i in range(len(nums) - 1):
            if nums[i] > nums[i + 1]:
                s = False

                break
        
        if s: return o

        m_s = nums[0] + nums[1]
        m_i = 0

        for i in range(1, len(nums) - 1):
            c_s = nums[i] + nums[i + 1]

            if c_s < m_s:
                m_s = c_s
                m_i = i
        
        nums[m_i] = m_s

        nums.pop(m_i + 1)

        o += 1 # (7 ms)