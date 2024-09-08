from math import sqrt, floor


class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        return int(floor(sqrt(x)))


print(Solution().mySqrt(4))