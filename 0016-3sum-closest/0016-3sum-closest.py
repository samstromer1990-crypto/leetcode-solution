import math

class Solution:
    def threeSumClosest(self, nums: list[int], target: int) -> int:
        nums.sort()  
        closer = math.e ** 50
        closest_sum = 0
        
        for i in range(len(nums) - 2):
            left = i + 1
            right = len(nums) - 1
            
            while left < right:
                
                a = [nums[i], nums[left], nums[right]]
                g = sum(a)
                
                small = abs(g - target)
                if small < closer:
                    closer = small
                    closest_sum = g
                
                
                if g < target:
                    left += 1
                elif g > target:
                    right -= 1
                else:
                    return g  
                    
        return closest_sum