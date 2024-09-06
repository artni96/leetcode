from math import log


class Solution(object):
    def isPowerOfFour(self, n):
        """
        :type n: int
        :rtype: bool
        """
        # более долгий вариант
        
        # start_power = 0
        # result = 0
        # while result <= n:
        #     result = 4 ** start_power
        #     if result == n:
        #         return True
        #     start_power += 1
        # return False
        if n > 0:
            if log(n, 4).is_integer():
                return True
        return False


test_data_1 = 16
test_data_2 = 5
test_data_3 = 1
print(Solution().isPowerOfFour(test_data_1))
print(Solution().isPowerOfFour(test_data_2))
print(Solution().isPowerOfFour(test_data_3))

