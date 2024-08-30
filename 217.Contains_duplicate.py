class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        return not (len(nums) == len(set(nums)))


test_1 = [1, 2, 3, 1]
print(Solution().containsDuplicate(test_1))
