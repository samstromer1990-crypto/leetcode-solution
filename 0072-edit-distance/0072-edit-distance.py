class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        memo = {}

        def solve(i, j):
            if i == 0: 
                return j
            if j == 0: 
                return i
            
            if (i, j) in memo: 
                return memo[(i, j)]
            
            if word1[i - 1] == word2[j - 1]:
                memo[(i, j)] = solve(i - 1, j - 1)
            else:
                insert = solve(i, j - 1)
                delete = solve(i - 1, j)
                replace = solve(i - 1, j - 1)
                
                memo[(i, j)] = 1 + min(insert, delete, replace)
                
            return memo[(i, j)]

        return solve(len(word1), len(word2))