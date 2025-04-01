class Solution:
    def search(self, nums: list[int], target: int) -> int:
        if not nums:
            return -1
        left = 0
        right = len(nums) - 1
        while left < right:
            mid = (left + right) // 2
            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid
        pivot = left
        left, right = 0, len(nums) - 1
        if target >= nums[pivot] and target <= nums[right]:
            left = pivot
        else:
            right = pivot
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1
        return -1

test_1 = [4, 5, 6, 7, 0, 1, 2]
target_1 = 0
print(Solution().search(test_1, target_1))
test_2 = [4, 5, 6, 7, 0, 1, 2]
target_2 = 3
print(Solution().search(test_2, target_2))
test_3 = [3, 1]
target_3 = 3
print(Solution().search(test_3, target_3))
