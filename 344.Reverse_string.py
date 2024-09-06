class Solution(object):
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        end_point = len(s) - 1
        for elem in range((len(s) - 1) // 2 + 1):
            s[end_point], s[elem] = s[elem], s[end_point]
            end_point -= 1
        return s


test_data_1 = ["h", "e", "l", "l", "o"]
test_data_2 = ["H", "a", "n", "n", "a", "h"]
print(Solution().reverseString(test_data_1))
print(Solution().reverseString(test_data_2))

test_data_3 = ["A"," ","m","a","n",","," ","a"," ","p","l","a","n",","," ","a"," ","c","a","n","a","l",":"," ","P","a","n","a","m","a"]
assert Solution().reverseString(test_data_3) == ["a","m","a","n","a","P"," ",":","l","a","n","a","c"," ","a"," ",",","n","a","l","p"," ","a"," ",",","n","a","m"," ","A"]
