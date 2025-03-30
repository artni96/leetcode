class Solution:
    def max_area(self, height: list[int]) -> int:
        max_volume = 0
        for elem_1 in range(len(height)):
            max_1 = height[elem_1]
            i_max_1 = elem_1
            for elem_2 in range(len(height)):
                max_2 = height[elem_2]
                i_max_2 = elem_2
                if max_1 > max_2:
                    current_height = max_2
                else:
                    current_height = max_1
                current_volume = current_height * abs(i_max_1 - i_max_2)
                if current_volume > max_volume:
                    max_volume = current_volume
        return max_volume




test_1 = [1,8,6,2,5,4,8,3,7]
Solution().max_area(test_1)
test_2 = [1, 1]
Solution().max_area(test_2)
