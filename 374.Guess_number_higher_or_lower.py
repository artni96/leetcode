def guess(num, picked_num):
    if num == picked_num:
        return 0
    elif num > picked_num:
        return -1
    return 1


class Solution(object):
    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        left = 1
        right = n
        while left <= right:
            mid = (left + right) // 2
            if guess(mid, picked_num) == 0:
                return mid
            elif guess(mid, picked_num) == -1:
                right = mid - 1
            elif guess(mid, picked_num) == 1:
                left = mid + 1


picked_num = 3
print(Solution().guessNumber(10))
