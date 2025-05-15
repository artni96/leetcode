class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        # k %= len(nums)
        # if len(nums) % 2 == 1 or len(nums) % 2 == 0:
        #     k = len(nums) - k
        # elif k % 2 == 1:
        #     k -= 2
        # formated_nums = nums[k:] + nums[:k]
        # for _ in range(len(nums)):
        #     nums[_] = formated_nums[_]
        k %= len(nums)
        l, r = 0, len(nums) - 1
        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l += 1
            r -= 1
        l, r = 0, k - 1
        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l += 1
            r -= 1
        l, r = k, len(nums) - 1
        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l += 1
            r -= 1
        return nums


test = [1, 2, 3, 4, 5, 6, 7]
assert Solution().rotate(test, 3) == [5, 6, 7, 1, 2, 3, 4]
test = [-1, -100, 3, 99]
assert Solution().rotate(test, 2) == [3, 99, -1, -100]
test = [1, 2, 3]
assert Solution().rotate(test, 4) == [3, 1, 2]
test = [1, 2, 3]
assert Solution().rotate(test, 2) == [2, 3, 1]
test = [-1, -100, 3, 99]
assert Solution().rotate(test, 3) == [-100, 3, 99, -1]
test = [1, 2, 3, 4, 5, 6]
assert Solution().rotate(test, 2) == [5, 6, 1, 2, 3, 4]
test = [1, 2]
print(Solution().rotate(test, 5))
