class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        result = ''
        if len(strs) == 0 or strs[0] == '':
            return result
        elif len(strs) == 1:
            return strs[0]
        obj_len_list = [
            [len(strs[obj_index]), obj_index] for obj_index in range(
                len(strs))
            ]
        obj_len_list.sort()
        subj = strs[obj_len_list[0][1]]
        current_result = ''
        sub_tail_index = 0
        while sub_tail_index <= len(subj) - 1:
            current_result += subj[sub_tail_index]
            count = 0
            for elem in strs:
                if current_result in elem:
                    count += 1
            if count != len(strs):
                if (
                    len(current_result) > len(result)
                ):
                    result = current_result[:sub_tail_index]
                if len(current_result) == 1:
                    sub_tail_index += 1
                current_result = ''
            else:
                sub_tail_index += 1
        if len(current_result) >= len(result):
            result = current_result
        return result


test_data_1 = ["flower", "flow", "flight"]
test_data_2 = ["dog", "racecar", "car"]
test_data_3 = ['']
test_data_4 = ['a']
test_data_5 = ['', '']
test_data_6 = ["ab", "a"]
print(Solution().longestCommonPrefix(test_data_1))
print(Solution().longestCommonPrefix(test_data_2))
print(Solution().longestCommonPrefix(test_data_3))
print(Solution().longestCommonPrefix(test_data_4))
print(Solution().longestCommonPrefix(test_data_5))
print(Solution().longestCommonPrefix(test_data_6))