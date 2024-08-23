class Solution(object):

    def decimail_to_binary(self, elem):
        result = ''
        while elem != 0:
            if elem % 2 == 0:
                result += '0'
                elem = elem // 2
            else:
                result += '1'
                elem = elem // 2
        return result[::-1]

    def get_coordinates_of_1(self, arr):
        coordinates = []
        for elem in range(len(arr)):
            if arr[elem] == '1':
                coordinates.append(elem)
        return coordinates

    def get_longest_gap(self, coordinates):
        start = 0
        end = start + 1
        longest_gap = 0
        if len(coordinates) == 0 or len(coordinates) == 1:
            return longest_gap
        else:
            while end < len(coordinates):
                if coordinates[end] - coordinates[start] > longest_gap:
                    longest_gap = coordinates[end] - coordinates[start]
                    start += 1
                    end = start + 1
                else:
                    start += 1
                    end = start + 1
            return longest_gap

    def binaryGap(self, n):
        """
        :type n: int
        :rtype: int
        """
        input = self.decimail_to_binary(n)
        coordinates = self.get_coordinates_of_1(input)
        return self.get_longest_gap(coordinates)

# input = decimail_to_binary(22)
# coordinates = get_coordinates_of_1(input)
# print(get_longest_gap(coordinates))
print(Solution().binaryGap(22))
