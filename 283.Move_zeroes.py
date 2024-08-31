class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        start = 0
        end = 1
        while end < len(nums):
            if nums[start] == 0 and nums[end] == 0:
                end += 1
            elif nums[start] == 0:
                nums[start] = nums[end]
                nums[end] = 0
                
                start += 1
                end += 1
            else:
                start = end
                end += 1
        


test_data_1 = [0, 1, 0, 3, 12]
print(Solution().moveZeroes(test_data_1))
