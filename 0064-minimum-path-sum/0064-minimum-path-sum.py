class Solution:
    def minPathSum(self, grid: list[list[int]]) -> int:

        rows = len(grid)
        cols = len(grid[0])
        dp = {}

        def solve(row, col):

            if row == rows - 1 and col == cols - 1:
                return grid[row][col]

            if (row, col) in dp:
                return dp[(row, col)]

            down = float('inf')
            right = float('inf')

            if row + 1 < rows:
                down = solve(row + 1, col)

            if col + 1 < cols:
                right = solve(row, col + 1)

            dp[(row, col)] = grid[row][col] + min(down, right)

            return dp[(row, col)]

        return solve(0, 0)