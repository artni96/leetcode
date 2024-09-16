class Solution(object):
    def validMountainArray(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        left = 0
        right = len(arr) - 1
        if len(arr) > 2:
            while left + 1 < len(arr) - 1 and arr[left] < arr[left + 1]:
                left += 1
            while right - 1 > 0 and arr[right] < arr[right - 1]:
                right -= 1
            if left == right:
                return True
        return False


test_data_1 = [0, 3, 2, 1]
test_data_2 = [3, 5, 5]
test_data_3 = []
test_data_4 = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
test_data_5 = [14,82,89,84,79,70,70,68,67,66,63,60,58,54,44,43,32,28,26,25,22,15,13,12,10,8,7,5,4,3]
print(Solution().validMountainArray(test_data_1))
print(Solution().validMountainArray(test_data_2))
print(Solution().validMountainArray(test_data_3))
print(Solution().validMountainArray(test_data_4))
print(Solution().validMountainArray(test_data_5))
