class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        start = 0
        end = 0
        for elem in range(len(s)):
            start += 1
            if set(s[start:end]) != len(s[start:end]):


# s = "pwwkew"
# s = "abcabcbb"
# s = "bbbb"
s = " "
print(Solution().lengthOfLongestSubstring(s))
