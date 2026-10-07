from itertools import combinations

class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        result = []
        for i in range(len(nums) + 1):
            for comb in combinations(nums, i):
                result.append(list(comb))
        return result