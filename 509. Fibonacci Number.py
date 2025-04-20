class Solution(object):
    def fib(self, n):
        """
        :type n: int
        :rtype: int
        """
        val = [0] * (n + 1)
        if n == 0:
            return 0
        elif n in (1, 2):
            return 1
        val[0], val[1] = 0, 1
        for i in range(2, n + 1):
            val[i] = val[i - 1] + val[i - 2]
        return val[n]
