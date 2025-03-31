class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        result = [intervals[0],]
        for cur_int in intervals[1:]:
            is_modified = False
            for res_interval in result:
                cur_res_range = range(res_interval[0], res_interval[1] + 1)
                if cur_int[0] in cur_res_range or cur_int[1] in cur_res_range:
                    if cur_int[0] in cur_res_range and cur_int[1] in cur_res_range:
                        break
                    if cur_int[0] in cur_res_range:
                        res_interval[1] = cur_int[1]

                    if cur_int[1] in cur_res_range:
                        res_interval[0] = cur_int[0]
                    is_modified = True
                else:
                    pass
            else:
                if not is_modified:
                    result.append(cur_int)
        return result


test_1 = [[1, 3],[2, 6],[8, 10],[15, 18]]
test_2 = [[2, 4], [3, 5], [1, 4], [6, 7]]
test_3 = [[1, 4],[4, 5]]
test_4 = [[1, 4], [2, 3]]
test_5 = [[1, 3], [2, 3], [2, 2], [2, 2], [3, 3], [4, 6], [5, 7]]
print(Solution().merge(test_2))
print(Solution().merge(test_1))
print(Solution().merge(test_3))
print(Solution().merge(test_4))
print(Solution().merge(test_5))