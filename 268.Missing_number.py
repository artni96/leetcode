class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = sorted(nums)
        left = 0
        right = len(nums)
        while left < right:
            mid = (left + right) // 2
            first_half = nums[left: mid]
            second_half = nums[mid: right]
            if len(nums) == 1:
                if nums[0] != 0:
                    return nums[0] - 1
            try:
                first_half_condition = first_half[-1] - first_half[0] == len(first_half) - 1
            except IndexError:
                first_half_condition = True
            try:
                second_half_condition = second_half[-1] - second_half[0] == len(second_half) - 1
            except IndexError:
                second_half_condition = True
            try:
                full_length_condition = nums[-1] - nums[0] == len(nums) - 1
            except IndexError:
                full_length_condition = True
            if full_length_condition:
                if nums[0] == 0:
                    return nums[-1] + 1
                return nums[0] - 1
            elif first_half_condition and second_half_condition:
                return second_half[0] - 1
            elif not first_half_condition:
                right = mid
            elif not second_half_condition:
                left = mid


test_data_1 = [19, 16, 14, 18, 13, 15, 17, 10, 11]
test_data_2 = [19, 16, 14, 18, 13, 15, 17, 10, 12]
test_data_3 = [19, 16, 14, 18, 13, 15, 17, 10, 12, 11]
test_data_4 = [3, 0, 1]
test_data_5 = [0]
test_data_6 = [1, 2]
test_data_7 = [11,47,30,16,48,8,33,32,13,21,42,36,45,3,17,43,27,6,12,26,14,18,24,39,0,15,5,23,22,10,38,7,34,49,40,46,2,25,19,4,37,41,28,31,20,9,1,35,44]
print(Solution().missingNumber(test_data_1))
print(Solution().missingNumber(test_data_2))
print(Solution().missingNumber(test_data_3))
print(Solution().missingNumber(test_data_4))
print(Solution().missingNumber(test_data_5))
print(Solution().missingNumber(test_data_6))
print(Solution().missingNumber(test_data_7))
