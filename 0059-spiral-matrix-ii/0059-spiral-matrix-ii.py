class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        matrix = [[0] * n for _ in range(n)]
        
        rows = n
        cols = n

        top = 0
        bottom = rows
        left = 0
        right = cols

        num = 1

        while num <= n * n:
            for j in range(left, right):
                matrix[top][j] = num
                num += 1
            top += 1

            if num > n * n:
                break

            for i in range(top, bottom):
                matrix[i][right - 1] = num
                num += 1
            right -= 1

            if num > n * n:
                break

            for j in range(right - 1, left - 1, -1):
                matrix[bottom - 1][j] = num
                num += 1
            bottom -= 1

            if num > n * n:
                break

            for i in range(bottom - 1, top - 1, -1):
                matrix[i][left] = num
                num += 1
            left += 1

        return matrix