class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        memo = {}

        def check(i, j):
            if (i, j) in memo:
                return memo[(i, j)]

            if j == len(p):
                return i == len(s)

            first_match = i < len(s) and (p[j] == s[i] or p[j] == '.')

            if j + 1 < len(p) and p[j + 1] == '*':
                result = check(i, j + 2) or (first_match and check(i + 1, j))
            
            elif first_match:
                result = check(i + 1, j + 1)
            else:
                result = False

            memo[(i, j)] = result
            return result

        return check(0, 0)