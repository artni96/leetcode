class Solution:
    def lists_diff(self, left: list[int], right: list[int]) -> list[int]:
        # if len(set(left)) >= len(set(right)):
        #     return list(set(left) - set(right))
        # return list(set(right) - set(left))
        return list(set(left) - set(right))

left = [1, 2]
right = [1, 2, 2, 3]
print(Solution().lists_diff(left, right))
