# https://leetcode.com/problems/walking-robot-simulation-ii/

class Robot:
    def __init__(self, width: int, height: int):
        self.w = width
        self.h = height
        self.cycle = 2 * (width + height) - 4
        self.moved_total = 0

    def step(self, num: int) -> None:
        self.moved_total += num

    def getPos(self) -> list[int]:
        steps = self.moved_total % self.cycle
        if steps <= self.w - 1:
            return [steps, 0]
        elif steps <= self.w + self.h - 2:
            return [self.w - 1, steps - (self.w - 1)]
        elif steps <= 2 * self.w + self.h - 3:
            return [self.w - 1 - (steps - (self.w + self.h - 2)), self.h - 1]
        else:
            return [0, self.h - 1 - (steps - (2 * self.w + self.h - 3))]

    def getDir(self) -> str:
        steps = self.moved_total % self.cycle

        if self.moved_total > 0 and steps == 0:
            return "South"
        
        if 1 <= steps <= self.w - 1:
            return "East"
        elif self.w <= steps <= self.w + self.h - 2:
            return "North"
        elif self.w + self.h - 1 <= steps <= 2 * self.w + self.h - 3:
            return "West"
        else:
            return "South" if steps > 0 else "East"
        
# (39 ms)