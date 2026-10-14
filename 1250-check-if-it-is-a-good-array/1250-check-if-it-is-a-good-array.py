import math
from functools import reduce

class Solution:
    def isGoodArray(self, nums: list[int]) -> bool:
        return reduce(math.gcd, nums) == 1