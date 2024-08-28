class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) > 0:
            result = 1
            if len(nums) == 1:
                return result
        else:
            result = 0
        tail_index = 1
        tail_elem = nums[tail_index]
        last_unique_elem_index = 1
        while tail_index < len(nums):
            tail_elem = nums[tail_index - 1]
            if tail_elem != nums[tail_index]:
                nums[last_unique_elem_index] = nums[tail_index]
                last_unique_elem_index += 1
                tail_index += 1
                result += 1
            else:
                tail_index += 1
        for elem in range(last_unique_elem_index, len(nums)):
            nums[elem] = '_'
        return result
        # return nums


test_data_1 = [1, 1, 2]
test_data_2 = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
test_data_3 = [1]
test_data_4 = [1, 1]
print(Solution().removeDuplicates(test_data_1))
print(Solution().removeDuplicates(test_data_2))
print(Solution().removeDuplicates(test_data_3))
print(Solution().removeDuplicates(test_data_4))
