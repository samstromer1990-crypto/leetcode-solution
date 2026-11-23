class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        if not nums:
            return 0

        num_set = set(nums)

        def check(n: int) -> bool:
            return (n + 1) in num_set

        def measure_group(start: int) -> int:
            length = 1
            curr = start
            num_set.discard(curr)

            while check(curr):
                curr += 1
                length += 1
                num_set.discard(curr)

            return length

        best_length = 0
        for num in list(num_set):
            if (num - 1) not in num_set and num in num_set:
                current_group_len = measure_group(num)
                if current_group_len > best_length:
                    best_length = current_group_len

        return best_length