class Solution:
    def maxDistinct(self, s: str) -> int:
        mask = 0
        res = 0
        for c in s:
            bit = 1 << (ord(c) - 97)
            if (mask & bit) == 0:
                mask |= bit
                res += 1
                if res == 26: break
        return res

        