class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        pfix = strs[0]
        pfix_len = len(pfix)

        for s in strs[1:]:
            while pfix != s[0:pfix_len]:
                pfix_len -= 1
                if pfix_len == 0:
                    return ""
                pfix = pfix[0:pfix_len]
        return pfix
        