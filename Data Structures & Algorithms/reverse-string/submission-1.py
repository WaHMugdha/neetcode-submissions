class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        # n = int(len(s)/2)
        # for i in range(n):
        #     s[i], s[len(s) - i - 1] = s[len(s) - i- 1], s[i]
        l = 0
        r = len(s) - 1
        while l < r:
            s[l], s[r] = s[r], s[l]
            l += 1
            r -= 1