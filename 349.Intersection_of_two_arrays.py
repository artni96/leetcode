class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        nums1 = set(nums1)
        nums2 = set(nums2)
        return list(set(nums1.intersection(nums2)))


test_data_1_nums1 = [1, 2, 2, 1]
test_data_1_nums2 = [2, 2]
print(Solution().intersection(test_data_1_nums1, test_data_1_nums2))
test_data_2_nums1 = [4, 9, 5]
test_data_2_nums2 = [9, 4, 9, 8, 4]
print(Solution().intersection(test_data_2_nums1, test_data_2_nums2))
