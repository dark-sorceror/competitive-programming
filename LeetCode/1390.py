# https://leetcode.com/problems/four-divisors/

def sumFourDivisors(nums: list[int]) -> int:
    t = 0
    
    def divisors(n):
        d = set()
        
        for i in range(1, int(n ** 0.5) + 1):
            if n % i == 0:
                d.add(i)
                d.add(n // i)
                
            if len(d) > 4: return 0
            
        if len(d) == 4:return sum(d)
        
        return 0

    for i in nums:
        t += divisors(i)
    
    return t # (191 ms)