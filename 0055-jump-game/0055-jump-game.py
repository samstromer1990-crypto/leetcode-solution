class Solution:
    def canJump(self, nums: List[int]) -> bool:

        g = 0

        for i in range(len(nums)):

            if i > g:
                return False

            g = max(g, i + nums[i])

            if g >= len(nums) - 1:
                return True

        return False