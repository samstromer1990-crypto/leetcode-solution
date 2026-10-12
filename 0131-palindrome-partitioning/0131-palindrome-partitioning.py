
class Solution:
    def partition(self, s: str) -> list[list[str]]:
        output = []
        par_output = []

        def solve(start):
            if start == len(s):
                output.append(par_output.copy())
                return

            a = ''

            for j in range(start, len(s)):
                a += s[j]
                rev = a[::-1]

                if a == rev:
                    par_output.append(a)
                    solve(j + 1)
                    par_output.pop()

        solve(0)
        return output