class Solution:
    def numTrees(self, n: int) -> int:
        dp = [0] * (n + 1)
        
        dp[0] = 1
        dp[1] = 1
        
        for nodes in range(2, n + 1):
            for i in range(1, nodes + 1):
                left_count = dp[i - 1]
                
                right_count = dp[nodes - i]
                
                dp[nodes] += left_count * right_count
                
        return dp[n]