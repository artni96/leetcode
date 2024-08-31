class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        result = [None, 0]
        for elem in nums:
            if result[0] is None or result[1] == 0:
                result[0] = elem
                result[1] += 1
            elif elem == result[0]:
                result[1] += 1
            elif elem != result[0]:
                result[1] -= 1
        return result[0]


test_data_1 = [2, 2, 1, 1, 1, 2, 2]
print(Solution().majorityElement(test_data_1))
