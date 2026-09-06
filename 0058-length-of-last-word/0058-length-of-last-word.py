class Solution:
    def lengthOfLastWord(self, s: str) -> int:

        output = []

        for i in range(len(s) - 1, -1, -1):

            if s[i] == ' ' and len(output) == 0:
                continue

            if s[i] == ' ':
                break

            output.append(s[i])

        return len(output)