class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for first_elem in range(0, len(nums)):
            for second_elem in range(first_elem + 1, len(nums)):
                if nums[first_elem] + nums[second_elem] == target:
                    return [first_elem, second_elem]


nums = [3, 3]
target = 6

obj = Solution().twoSum(nums, target)
print(obj)
