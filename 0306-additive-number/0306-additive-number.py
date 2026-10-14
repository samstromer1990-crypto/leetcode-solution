class Solution:
    def isAdditiveNumber(self, num: str) -> bool:
        n = len(num)

        for i in range(1, n):
            for j in range(i + 1, n):
                first = num[:i]
                second = num[i:j]

                if len(first) > 1 and first[0] == '0':
                    break
                if len(second) > 1 and second[0] == '0':
                    continue

                a = int(first)
                b = int(second)
                k = j

                while k < n:
                    total = str(a + b)

                    if not num.startswith(total, k):
                        break

                    k += len(total)
                    a, b = b, int(total)

                if k == n:
                    return True

        return False