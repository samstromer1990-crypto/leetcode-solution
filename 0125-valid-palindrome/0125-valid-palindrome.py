class Solution:
    def isPalindrome(self, s: str) -> bool:
        def nothing(text: str) -> str:
            r = ""
            for ch in text:
                if ch.isalnum():
                    r += ch
            return r

        cleaned = nothing(s).lower()

        def Output(seq: str) -> bool:
            i = 0
            j = len(seq) - 1
            while i < j:
                if seq[i] != seq[j]:
                    return False
                i += 1
                j -= 1
            return True

        return Output(cleaned)