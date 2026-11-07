class Solution:
    def search(self, nums: List[int], target: int) -> int:
        a = len(nums)
        b = a // 2

        if nums[b] == target:
            return b

        if nums[0] < nums[b]:

            if target >= nums[0] and target <= nums[b]:
                for i in range(0, b):
                    if nums[i] == target:
                        return i
            else:
                for i in range(b, a):
                    if nums[i] == target:
                        return i

        else:

            if target >= nums[b] and target <= nums[-1]:
                for i in range(b, a):
                    if nums[i] == target:
                        return i
            else:
                for i in range(0, b):
                    if nums[i] == target:
                        return i

        return -1