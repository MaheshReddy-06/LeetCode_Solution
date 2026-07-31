class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        common_prefix = ""
        strs = sorted(strs)
        i = 0
        length = len(strs)

        while i < len(strs[0]):
            if strs[0][i] == strs[length - 1][i]:
                common_prefix += strs[0][i]
            else:
                break
            i += 1
        return common_prefix



        