class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix)

        output = []

        for i in range(n):
            for j in range(n - 1, -1, -1):
                output.append(matrix[j][i])

        k = 0

        for i in range(n):
            for j in range(n):
                matrix[i][j] = output[k]
                k += 1