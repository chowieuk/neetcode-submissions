from functools import cache
# you can climb 1 or 2 steps at a time
class Solution:
    @cache
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n
        else:
            return self.climbStairs(n - 1) + self.climbStairs(n - 2)