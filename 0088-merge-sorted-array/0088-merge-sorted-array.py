class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        def remove_zero(lis):
            non_zero = []
            for i in range(len(lis)):
                if lis[i] == 0:
                    continue
                else:
                    non_zero.append(lis[i])  
            return non_zero

        def include_zero(List, a):
            if len(List) == a:
                return List
            else:
                diff = abs(len(List) - a)
                for j in range(diff):
                    List.append(0)
            return List                       

        def combine(lst1, lst2):
            for i in lst2:
                lst1.append(i)
            return lst1                       

        num1 = remove_zero(nums1[:m])
        num2 = remove_zero(nums2[:n])

        num1 = include_zero(num1, m)
        num2 = include_zero(num2, n)
        
        result = combine(num1, num2)
        result.sort()
        
        nums1[:] = result