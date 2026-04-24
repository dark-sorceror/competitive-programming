from collections import defaultdict

def distance(nums: list[int]) -> list[int]:
    m = defaultdict(list)
    
    for i, val in enumerate(nums):
        m[val].append(i)
        
    a = [0] * len(nums)
    
    for val, indices in m.items():
        k = len(indices)
        
        if k <= 1: continue
            
        total_sum = sum(indices)
        prefix_sum = 0
        
        for i, idx in enumerate(indices):
            l = i * idx - prefix_sum
            r = (total_sum - prefix_sum - idx) - (k - 1 - i) * idx
            
            a[idx] = l + r
            
            prefix_sum += idx
            
    return a # (95 ms)