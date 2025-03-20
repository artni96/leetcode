class Solution:
    def is_anagram(self, s: str, t: str) -> bool:
        return True if sorted(s) == sorted(t) else False

s = "anagram"
t = "nagaram"
print(Solution().is_anagram(s=s, t=t))
