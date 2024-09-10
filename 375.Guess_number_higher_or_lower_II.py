class Solution(object):
    def getMoneyAmount(self, n):
        """
        :type n: int
        :rtype: int
        """
        left = 1
        right = 10
        while left <= right:
            mid = (left + right) // 2
            left_side = range(left, mid)
            right_side = range(mid, right + 1)
            left_sum = sum(left_side)
            right_sum = sum(right_side)
            if left_sum < right_sum:
                if (right_sum - left_sum) > 2*right_side[0]:
                    left += 1


print(Solution().getMoneyAmount(10))
