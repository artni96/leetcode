class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        first_point = 0
        last_point = len(nums) - 1
        center_point = len(nums) // 2
        if nums[first_point] == target:
            return first_point
        elif nums[last_point] == target:
            return last_point
        elif target > nums[last_point]:
            return last_point + 1
        elif target < nums[first_point]:
            return 0
        elif len(nums) == 2:
            return first_point + 1
        while first_point < center_point < last_point:
            first_half = nums[first_point:center_point]
            second_half = nums[center_point:len(nums)]
            if target <= first_half[-1]:
                if target in first_half:
                    if target == first_half[0]:
                        return first_point
                    elif target == first_half[-1]:
                        return center_point - 1
                    elif len(first_half) == 2:
                        return first_point + 1
                    else:
                        last_point = center_point
                        center_point = (first_point + last_point) // 2
                else:
                    last_point = center_point
                    center_point = (first_point + last_point) // 2
            elif target >= second_half[0]:
                if target in second_half:
                    if target == second_half[0]:
                        return center_point
                    elif target == second_half[-1]:
                        return last_point
                    else:
                        first_point = center_point
                        center_point = (center_point + last_point) // 2
                elif len(second_half) == 2:
                    return center_point + 1
                else:
                    first_point = center_point
                    center_point = (center_point + last_point) // 2
            elif target >= second_half[0]:
                pass
            elif target > first_half[-1] and target < second_half[0]:
                return center_point


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
test_data_7_target = 0
test_data_8_nums = [1, 3, 5]
test_data_8_target = 4



# print(Solution().searchInsert(test_data_1_nums, test_data_1_target))
# print(Solution().searchInsert(test_data_2_nums, test_data_2_target))
# print(Solution().searchInsert(test_data_3_nums, test_data_3_target))
# print(Solution().searchInsert(test_data_3_nums, test_data_4_target))
# print(Solution().searchInsert(test_data_3_nums, test_data_5_target))
# print(Solution().searchInsert(test_data_3_nums, test_data_6_target))
# print(Solution().searchInsert(test_data_3_nums, test_data_7_target))
print(Solution().searchInsert(test_data_8_nums, test_data_8_target))
