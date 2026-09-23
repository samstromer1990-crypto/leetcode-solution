class Solution:
    def maxSum(self, nums1: list[int], nums2: list[int]) -> int:
        MAX = 0

        i = 0
        j = 0

        sum_1 = 0
        sum_2 = 0

        while i < len(nums1) and j < len(nums2):

            if nums1[i] < nums2[j]:
                sum_1 += nums1[i]
                i += 1

            elif nums1[i] > nums2[j]:
                sum_2 += nums2[j]
                j += 1

            else:
            
                MAX += max(sum_1, sum_2) + nums1[i]

                sum_1 = 0
                sum_2 = 0

                i += 1
                j += 1

        while i < len(nums1):
            sum_1 += nums1[i]
            i += 1

        while j < len(nums2):
            sum_2 += nums2[j]
            j += 1

        MAX += max(sum_1, sum_2)

        return MAX % (10**9 + 7)