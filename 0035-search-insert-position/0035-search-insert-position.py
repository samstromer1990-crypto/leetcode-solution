class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        a = len(nums)
        b = a // 2

        if nums[b] == target:
            return b

       
        if target > nums[b]:
            for i in range(b + 1, a):
                if nums[i] >= target:
                    return i
            return a  
       
        else:
            for i in range(0, b):
                if nums[i] >= target:
                    return i
            return b  
        
