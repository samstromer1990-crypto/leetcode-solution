class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:

        def get_val(index: int, cols: int) -> int:
            row = index // cols
            col = index % cols
            return matrix[row][col]


        if not matrix or not matrix[0]:
            return False

        rows = len(matrix)
        cols = len(matrix[0])
        left = 0
        right = (rows * cols) - 1


        while left <= right:
            mid = (left + right) // 2
            val = get_val(mid, cols)

            if val == target:
                return True
            elif val < target:
                left = mid + 1
            else:
                right = mid - 1

        return False