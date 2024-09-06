class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        # result = dict.fromkeys(set(s), 0)
        result = dict()
        index = 0
        for elem in s:
            if elem not in result:
                result[elem] = dict(index=index, count=1)
                
            elif elem in result:
                result[elem]['count'] += 1
            index += 1
        result_list = [(result[elem]['index'], elem) for elem in result if result[elem]['count'] == 1]
        try:
            return sorted(result_list)[0][0]
        except IndexError:
            return -1


test_data_1 = "leetcode"
test_data_2 = "loveleetcode"
test_data_3 = "aabb"
test_data_4 = "dddccdbba"
print(Solution().firstUniqChar(test_data_1))
print(Solution().firstUniqChar(test_data_2))
print(Solution().firstUniqChar(test_data_3))
print(Solution().firstUniqChar(test_data_4))
