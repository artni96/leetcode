class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        count = 0
        if len(s) > 0:
            return True
        for elem in t:
            if s[count] == elem:
                count += 1
            if count == len(s):
                return True
        if count == len(s):
            return True
        return False


test_data_1_s = 'abc'
test_data_1_t = 'ahbgdc'
test_data_2_s = 'axc'
test_data_2_t = 'ahbgdc'
test_data_3_s = ''
test_data_3_t = ''
test_data_4_s = ''
test_data_4_t = 'ahbgdc'
print(Solution().isSubsequence(test_data_1_s, test_data_1_t))
print(Solution().isSubsequence(test_data_2_s, test_data_2_t))
print(Solution().isSubsequence(test_data_3_s, test_data_3_t))
print(Solution().isSubsequence(test_data_4_s, test_data_4_t))
