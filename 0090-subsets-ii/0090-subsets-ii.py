import itertools

class Solution:
    def subsetsWithDup(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        output = set()
        for i in range(len(nums) + 1):
            for j in itertools.combinations(nums, i):
                output.add(j)
        return [list(j) for j in output]