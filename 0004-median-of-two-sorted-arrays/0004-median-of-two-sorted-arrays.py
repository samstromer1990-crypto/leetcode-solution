import numpy as np
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        
        merg = nums1 + nums2
        sort_merg = sorted(merg)
        if len(merg)%2 == 0:
            new_merg = np.median(sort_merg)
            return new_merg
        else:
            new_merg = np.median(sort_merg)
            return int(new_merg)