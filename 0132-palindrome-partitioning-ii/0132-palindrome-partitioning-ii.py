
class Solution:
    def minCut(self, s: str) -> int:

        n = len(s)
        is_pal = [[False] * n for _ in range(n)]

        ending_groups = [[] for _ in range(n)]

        for length in range(1, n + 1):

            for start in range(n - length + 1):

                end = start + length - 1

                if s[start] == s[end] and (
                    length <= 2 or is_pal[start + 1][end - 1]
                ):

                    is_pal[start][end] = True

                    ending_groups[end].append(
                        (start, end)
                    )
        dp = [float('inf')] * (n + 1)

        dp[0] = 0

        for end in range(n):

            for start, finish in ending_groups[end]:

                dp[end + 1] = min(
                    dp[end + 1],
                    dp[start] + 1
                )


        return dp[n] - 1