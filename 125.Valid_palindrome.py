class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        result_string = ''.join([elem.lower() for elem in s if elem.isalpha() is True or elem.isdigit()])
        return result_string == result_string[::-1]


test_data_1 = "A man, a plan, a canal: Panama"
test_data_2 = "race a car"
test_data_3 = ' '
test_data_4 = '0P'
print(Solution().isPalindrome(test_data_1))
print(Solution().isPalindrome(test_data_2))
print(Solution().isPalindrome(test_data_3))
print(Solution().isPalindrome(test_data_4))
