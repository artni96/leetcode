class Solution(object):
    def third_max(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 2:
            if nums[0] <= nums[1]:
                return nums[1]
            return nums[0]
        elif len(nums) >= 3:
            first_max, second_max, third_max = None, None, None
            for num in nums:
                if num != first_max and num != second_max and num != third_max:
                    if not first_max:
                        first_max = num
                    elif not second_max:
                        if num > first_max:
                            second_max = first_max
                            first_max = num
                        else:
                            second_max = num
                    elif not third_max:
                        if num > first_max:
                            third_max = second_max
                            second_max = first_max
                            first_max = num
                        elif num > second_max:
                            third_max = second_max
                            second_max = num
                        else:
                            third_max = num
                    elif num > first_max:
                        third_max = second_max
                        second_max = first_max
                        first_max = num
                    elif num > second_max:
                        third_max = second_max
                        second_max = num
                    elif num > third_max:
                        third_max = num
            if third_max is None:
                return first_max
            return third_max

        return nums[0]

test_list = [3,3,4,3,4,3,0,3,3]
print(Solution().third_max(test_list))
