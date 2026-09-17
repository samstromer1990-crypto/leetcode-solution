class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        
        def list_to_num(idx, current_num):
            if idx == len(digits):
                return current_num
            return list_to_num(idx + 1, current_num * 10 + digits[idx])

        def num_to_list(num):
            if num == 0:
                return []
            return num_to_list(num // 10) + [num % 10]

        total = list_to_num(0, 0) + 1
        return num_to_list(total)