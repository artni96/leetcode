class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        while n >= 5:
            current_result = 0
            for elem in str(n):
                current_result += int(elem)**2
            n = int(current_result)
        if n == 1:
            return True
        return False


test_data_1 = 6
print(Solution().isHappy(test_data_1))
