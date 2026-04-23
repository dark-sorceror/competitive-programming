# https://leetcode.com/problems/furthest-point-from-origin/

def furthestDistanceFromOrigin(moves: str) -> int:
    return abs(moves.count('L') - moves.count('R')) + moves.count('_') # (0 ms)