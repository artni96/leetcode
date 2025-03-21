class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        # first_point = 0
        # last_point = len(nums) - 1
        # while first_point <= last_point:
        #     center_point = (first_point + last_point) // 2
        #
        #     if nums[center_point] == target:
        #         return center_point
        #     elif target < nums[center_point]:
        #         last_point = center_point - 1
        #     else:
        #         first_point = center_point + 1
        # return first_point


        first_point = 0
        last_point = len(nums) - 1
        while first_point <= last_point:
            center_point = (first_point + last_point) // 2
            if target == nums[center_point]:
                return center_point
            elif target < nums[center_point]:
                last_point = center_point - 1
            else:
                first_point = center_point + 1
        return first_point





test_data_1_nums = [1, 3, 5, 6]
test_data_1_target = 5
test_data_2_nums = [1, 3, 5, 6]
test_data_2_target = 2
test_data_3_nums = [1, 3, 5, 7, 9, 11]
test_data_3_target = 9
test_data_4_target = 10
test_data_5_target = 12
test_data_6_target = 0
test_data_7_target = 2
# test_data_7_target = 5
# test_data_7_target = 3
# test_data_7_target = 8
# test_data_7_target = 9
# test_data_7_target = 0
test_data_8_nums = [1, 3, 5]
test_data_8_target = 4



# print(Solution().searchInsert(test_data_1_nums, test_data_1_target))
print(Solution().searchInsert(test_data_2_nums, test_data_2_target))
# print(Solution().searchInsert(test_data_3_nums, test_data_3_target))
# print(Solution().searchInsert(test_data_3_nums, test_data_4_target))
# print(Solution().searchInsert(test_data_3_nums, test_data_5_target))
# print(Solution().searchInsert(test_data_3_nums, test_data_6_target))
# print(Solution().searchInsert(test_data_3_nums, test_data_7_target))
# print(Solution().searchInsert(test_data_8_nums, test_data_8_target))
