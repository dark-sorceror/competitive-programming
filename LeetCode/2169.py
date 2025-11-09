# https://leetcode.com/problems/count-operations-to-obtain-zero/

def countOperations(num1: int, num2: int) -> int:
    s = 0
    
    while num1 and num2:
        if num1 >= num2:
            s += num1 // num2
            num1 %= num2
        else:
            s += num2 // num1
            num2 %= num1
        
    return s # (0 ms)