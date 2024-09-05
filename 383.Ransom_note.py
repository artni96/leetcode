class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        ransomNote = list(ransomNote)
        magazine = list(magazine)
        count = len(ransomNote)
        for elem in ransomNote:
            if elem in magazine:
                magazine.remove(elem)
                count -= 1
        if count == 0:
            return True
        return False


print(Solution().canConstruct('a', 'b'))
print(Solution().canConstruct('aa', 'ab'))
print(Solution().canConstruct('aab', 'baa'))
