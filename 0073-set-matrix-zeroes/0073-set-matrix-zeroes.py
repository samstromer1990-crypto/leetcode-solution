class Solution:
    def setZeroes(self, matrix: list[list[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        matrix_copy = [row[:] for row in matrix]        
        length_i = len(matrix)
        length_j = len(matrix[0])
        for i in range(length_i):
            for j in range(length_j):
                if matrix_copy[i][j] == 0:
                    for r in range(length_i):
                        matrix[r][j] =matrix[r][j]*0

                    for t in range(length_j):
                        matrix[i][t] =matrix[i][t]*0


