class Solution(object):
    def minNumberOperations(self, target):
        """
        :type target: List[int]
        :rtype: int
        """
        
        operations = 0
        prev = 0

        for i in target:
            d = i - prev

            if d > 0:
                operations += d

            prev = i
        
        return operations