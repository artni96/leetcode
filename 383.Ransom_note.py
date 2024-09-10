class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        # ransomNote = list(ransomNote)
        # magazine = list(magazine)
        # count = len(ransomNote)
        # for elem in ransomNote:
        #     if elem in magazine:
        #         magazine.remove(elem)
        #         count -= 1
        # if count == 0:
        #     return True
        # return False
        ransomNote = sorted(list(ransomNote))
        magazine = sorted(list(magazine))
        count = 0
        result = 0
        while result < len(ransomNote):
            try:
                if ransomNote[count] == magazine[count]:
                    result += 1
                count += 1
            except IndexError:
                return False
        return True
 

# print(Solution().canConstruct('a', 'b'))
# print(Solution().canConstruct('aa', 'ab'))
# print(Solution().canConstruct('aab', 'baa'))
print(Solution().canConstruct('bg', "efjbdfbdgfjhhaiigfhbaejahgfbbgbjagbddfgdiaigdadhcfcj"))
