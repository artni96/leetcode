class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        result = 0
        tail_index = 0
        delta = 0
        while tail_index < len(nums):
            if nums[tail_index] == val:
                delta += 1
                tail_index += 1
            else:
                if len(nums) != tail_index:
                    if delta > 0:
                        nums[tail_index - delta] = nums[tail_index]
                        # nums[tail_index] = '_'
                        
                    result += 1
                    tail_index += 1
        for i in range(len(nums) - delta, len(nums)):
            nums[i] = '_'
        return result


test_data_nums_1 = [3, 2, 2, 3]
test_data_val_1 = 3
test_data_nums_2 = [0, 1, 2, 2, 3, 0, 4, 2]
test_data_val_2 = 2
print(Solution().removeElement(test_data_nums_1, test_data_val_1))
print(Solution().removeElement(test_data_nums_2, test_data_val_2))
