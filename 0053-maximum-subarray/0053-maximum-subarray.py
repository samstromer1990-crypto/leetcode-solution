class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        total = nums[0]
        max_total = nums[0]

        for i in range(1, len(nums)):

            if total + nums[i] < nums[i]:
                total = nums[i]
            else:
                total += nums[i]

            if total > max_total:
                max_total = total

        return max_total