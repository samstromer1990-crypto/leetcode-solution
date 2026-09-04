class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        prefix = []
        # zip(*strs) groups characters by column index
        for chars in zip(*strs):
            # If all strings have the same character at this index, len(set) will be 1
            if len(set(chars)) == 1:
                prefix.append(chars[0])
            else:
                break
        return "".join(prefix)