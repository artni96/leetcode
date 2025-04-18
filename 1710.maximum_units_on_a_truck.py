class Solution(object):
    def maximumUnits(self, boxTypes, truckSize):
        """
        :type boxTypes: List[List[int]]
        :type truckSize: int
        :rtype: int
        """
        result = 0
        box_counter = 0
        boxTypes = sorted(boxTypes, key=lambda x: x[1], reverse=True)
        for elem in boxTypes:
            box_counter += elem[0]
            result += (elem[0] * elem[1])
            if box_counter > truckSize:
                to_minus = abs(truckSize - box_counter)
                box_counter -= to_minus
                result -= (to_minus * elem[1])
        return result

data = [[1, 3], [2, 2], [3, 1]]
print(Solution().maximumUnits(data, 4))
data = [[5,10],[2,5],[4,7],[3,9]]
print(Solution().maximumUnits(data, 10))