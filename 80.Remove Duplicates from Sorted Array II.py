class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        cur_elem = nums[0]
        cur_counter = 1
        cursor = 1
        coef = 0
        for i in range(1, len(nums)):
            if cur_elem == nums[i]:
                if cur_counter <= 1:
                    nums[cursor] = nums[i]
                    cursor += 1
                else:
                    coef += 1
                cur_counter += 1

            else:
                cur_counter = 1
                cur_elem = nums[i]
                nums[cursor] = nums[i]
                cursor += 1
        for _ in range(len(nums) - coef, len(nums)):
            nums[_] = "_"
        return nums


test = [1, 1, 1, 2, 2, 3]
print(Solution().removeDuplicates(test))
test = [0,0,1,1,1,1,2,3,3]
print(Solution().removeDuplicates(test))

