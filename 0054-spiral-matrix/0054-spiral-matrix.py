class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:

        rows = len(matrix)
        cols = len(matrix[0])

        output = []

        top = 0
        bottom = rows
        left = 0
        right = cols

        while len(output) < rows * cols:

            for j in range(left, right):
                output.append(matrix[top][j])

            top += 1

            if len(output) == rows * cols:
                break

            for i in range(top, bottom):
                output.append(matrix[i][right - 1])

            right -= 1

            if len(output) == rows * cols:
                break

            for j in range(right - 1, left - 1, -1):
                output.append(matrix[bottom - 1][j])

            bottom -= 1

            if len(output) == rows * cols:
                break

            
            for i in range(bottom - 1, top - 1, -1):
                output.append(matrix[i][left])

            left += 1

        return output