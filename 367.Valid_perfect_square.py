class Solution(object):
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """

        if num == 1:
            return True
        left = 1
        right = num
        while left < right:
            mid = (left + right) // 2
            if mid*mid == num:
                return True
            elif mid*mid > num:
                right = mid
            elif mid*mid < num:
                left = mid + 1
        return False


test_data_1 = 1
test_data_2 = 104976
test_data_3 = 4
print(Solution().isPerfectSquare(test_data_1))
print(Solution().isPerfectSquare(test_data_2))
print(Solution().isPerfectSquare(test_data_3))
