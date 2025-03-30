import math

class Solution:
    def product_except_self(self, nums: list[int]) -> list[int]:
        # Напишите здесь свой код
        result = list()
        for i in range(len(nums)):
            print(f"i = {i}")
            if i - 1 < 0:
                right_half = nums[i+1:]
                right_result = math.prod(right_half)
                left_result = 1
            else:
                left_half, right_half = nums[:i], nums[i+1:]
                left_result = math.prod(left_half)
                right_result = math.prod(right_half)
            result.append(left_result * right_result)
        return result


test_1 = [1, 2, 3, 4]
print(Solution().product_except_self(test_1))