class Solution:
    def search(self, nums: list[int], target: int) -> bool:
        mid =  len(nums)//2
        nums.sort()
        if target < nums[mid]:
            for i in range(0,mid):
                if target == nums[i]:
                    return True
                else:
                    continue
        else:
            for i in range(mid,len(nums)):
                if target == nums[i]:
                    return True
                else:
                    continue
        return False