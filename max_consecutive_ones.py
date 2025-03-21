class Solution:
    def find_max_consecutive_ones(self, nums: list[int]) -> int:
        max_count = 0
        current_count = 0
        for elem in nums:
            if elem == 0:
                if current_count > max_count:
                    max_count = current_count
                current_count = 0
            else:
                current_count += 1
        return max_count if max_count > current_count else current_count


test_1 = [1, 1, 0, 1, 1, 1]
test_2 = [1, 0, 1, 1, 0, 1]
print(Solution().find_max_consecutive_ones(test_1))
print(Solution().find_max_consecutive_ones(test_2))
