class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # hash_table = dict.fromkeys(set(nums), 1)
        # for elem in nums:
        #     if elem not in hash_table.keys():
        #         hash_table[elem] = 1
        #     else:
        #         del hash_table[elem]
        # return list(hash_table.keys())[0]
        result = 0
        for num in nums:
            result ^= num
        return result




test_data_1 = [2, 2, 1]
test_data_2 = [4, 1, 2, 1, 2]
test_data_3 = [1, 2, 3, 2, 1, 3]
print(Solution().singleNumber(test_data_1))
print(Solution().singleNumber(test_data_2))
print(Solution().singleNumber(test_data_3))
