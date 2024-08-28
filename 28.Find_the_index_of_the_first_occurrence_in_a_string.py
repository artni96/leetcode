class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """

        # if needle in haystack:  RT - 17.51%, M - 84.54%
        #     start_point = 0
        #     end_point = len(needle)
        #     while end_point != len(haystack) and start_point < end_point:
        #         current_obj = haystack[start_point: end_point]
        #         if needle == current_obj:
        #             return start_point
        #         else:
        #             start_point += 1
        #             end_point += 1
        #     return start_point
        # return -1

        start_point = 0  # RT - 90.66%, M - 84.54%
        end_point = len(needle)
        while end_point <= len(haystack):
            if needle == haystack[start_point:end_point]:
                return start_point
            start_point += 1
            end_point += 1
        return -1


test_data_1_haystack = 'sadbutsad'
test_data_1_needle = 'sad'
test_data_2_haystack = 'leetcode'
test_data_2_needle = 'leeto'
test_data_3_haystack = 'a'
test_data_3_needle = 'a'
test_data_4_haystack = 'hello'
test_data_4_needle = 'll'
test_data_5_haystack = 'abc'
test_data_5_needle = 'c'

print(Solution().strStr(test_data_1_haystack, test_data_1_needle))
print(Solution().strStr(test_data_2_haystack, test_data_2_needle))
print(Solution().strStr(test_data_3_haystack, test_data_3_needle))
print(Solution().strStr(test_data_4_haystack, test_data_4_needle))
print(Solution().strStr(test_data_5_haystack, test_data_5_needle))
