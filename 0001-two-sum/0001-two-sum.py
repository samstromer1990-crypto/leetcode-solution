class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        # Loop through every element using its index
        for i in range(len(nums)):
            # Loop through the elements after the i-th element
            for j in range(i + 1, len(nums)):
                # Check if the values at these indices add up to the target
                if nums[i] + nums[j] == target:
                    return [i, j]  # Return the indices as a list