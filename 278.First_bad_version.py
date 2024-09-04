def isBadVersion(version, bad):
    return version == bad


class Solution(object):
    def firstBadVersion(self, n, bad):
        """
        :type n: int
        :rtype: int
        """
        left = 1
        right = n 
        while left < right:
            mid = (left + right) // 2
            if isBadVersion(mid, bad):
                if not isBadVersion(mid - 1, bad):
                    return mid
                right = mid + 1
            elif not isBadVersion(mid, bad):
                left = mid


print(Solution().firstBadVersion(2, 1))
