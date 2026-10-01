class Solution:
    def setZeroes(self, matrix: list[list[int]]) -> None:

        matrix_copy = [row[:] for row in matrix]

        rows = len(matrix)
        cols = len(matrix[0])

        def make_row_zero(i):
            for j in range(cols):
                matrix[i][j] = 0

        def make_col_zero(j):
            for i in range(rows):
                matrix[i][j] = 0

        for i in range(rows):
            for j in range(cols):

                if matrix_copy[i][j] == 0:
                    make_row_zero(i)
                    make_col_zero(j)