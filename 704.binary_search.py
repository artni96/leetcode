class Solution:
    def search(self, nums, target):
        start, end = 0, len(nums)
        mid = (start + end) // 2
        while start < end:
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                end = mid
                mid = (start + end) // 2
            elif nums[mid] < target:
                start = mid + 1
                mid = (start + end) // 2
        return -1


x = [-1, 0, 3, 5, 9, 12]
solution = Solution().search(x, 2)
print(solution)
