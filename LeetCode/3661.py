# https://leetcode.com/problems/maximum-walls-destroyed-by-robots/

from bisect import bisect_left, bisect_right
from typing import List

def maxWalls(robots: List[int], distance: List[int], walls: List[int]) -> int:
    unique_walls = set(walls)
    robot_pos_set = set(robots)
    
    walls_on_robots = len(unique_walls.intersection(robot_pos_set))
    filtered_walls = sorted(list(unique_walls - robot_pos_set))
    
    sorted_robots = sorted(zip(robots, distance))
    n = len(sorted_robots)
    
    def count_walls(A: int, B: int) -> int:
        if A > B:
            return 0
        return bisect_right(filtered_walls, B) - bisect_left(filtered_walls, A)

    P0, D0 = sorted_robots[0]
    dp_L = count_walls(P0 - D0, P0 - 1)
    dp_R = 0 

    for i in range(1, n):
        P_prev, D_prev = sorted_robots[i-1]
        P_curr, D_curr = sorted_robots[i]
        
        I_R_end = min(P_curr - 1, P_prev + D_prev)
        I_L_start = max(P_prev + 1, P_curr - D_curr)
        
        count_R = count_walls(P_prev + 1, I_R_end)
        count_L = count_walls(I_L_start, P_curr - 1)
        
        if I_R_end >= I_L_start:
            count_RL = count_walls(P_prev + 1, P_curr - 1)
        else:
            count_RL = count_R + count_L
            
        new_dp_L = max(dp_L + count_L, dp_R + count_RL)
        
        new_dp_R = max(dp_L + 0, dp_R + count_R)
        
        dp_L, dp_R = new_dp_L, new_dp_R

    P_last, D_last = sorted_robots[-1]
    count_last_R = count_walls(P_last + 1, P_last + D_last)
    
    return walls_on_robots + max(dp_L, dp_R + count_last_R) # (611 ms)