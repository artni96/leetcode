class Solution:
    def search(self, nums: list[int], target: int) -> int:
        mid_index = len(nums) // 2
        left_half, right_half = nums[:mid_index], nums[mid_index:]
        print(left_half)
        print(right_half)
        if right_half[0] <= target < right_half[-1]:
            for elem in right_half:
                if elem == target:
                    return elem
        else:
            for elem in left_half:
                if elem == target:
                    return elem
        return -1



test_1 = [4, 5, 6, 7, 0, 1, 2]
test_target_1 = 0
print(Solution().search(nums=test_1, target=test_target_1))
