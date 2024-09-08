class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1:
            return 1
        if n == 2:
            return 2
        if n > 2:
            result = [1, 2]
            for i in range(3, n):
                new_result = int(result[-1] + result[-2])
                result[-2] = result[-1]
                result[-1] = new_result
                i += 1
            return int(result[-1] + result[-2])


test_data_1 = 5
print(Solution().climbStairs(test_data_1))
