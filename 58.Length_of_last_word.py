class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        return len([elem for elem in s.split(' ') if elem != ''][-1])


test_data_1 = "Hello World"
test_data_2 = "   fly me   to   the moon  "
test_data_3 = "luffy is still joyboy"
print(Solution().lengthOfLastWord(test_data_1))
print(Solution().lengthOfLastWord(test_data_2))
print(Solution().lengthOfLastWord(test_data_3))
