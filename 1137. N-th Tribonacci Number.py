class Solution(object):
    def tribonacci(self, n):
        """
        :type n: int
        :rtype: int
        """
        val = [0]*(n+1)
        if n == 0:
            return 0
        elif n in (1, 2):
            return 1
        val[0], val[1], val[2] = 0, 1, 1
        for i in range(3, n + 1):
            val[i] = val[i - 1] + val[i - 2] + val[i - 3]
        return val[n]


print(Solution().tribonacci(30))
