class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        triangle_layers_data = dict()
        if numRows > 0:
            if numRows >= 1:
                triangle_layers_data[1] = [1]
            if numRows >= 2:
                triangle_layers_data[2] = [1, 1]
            if numRows >= 3:
                for layer in range(3, numRows + 1):
                    first_elem = 0
                    second_elem = first_elem + 1
                    current_result = [1]
                    while second_elem <= len(triangle_layers_data[layer - 1]) - 1:
                        print(triangle_layers_data[layer - 1][0])
                        current_result.append(
                            triangle_layers_data[layer - 1][first_elem] +
                            triangle_layers_data[layer - 1][second_elem]
                        )
                        first_elem += 1
                        second_elem = first_elem + 1
                    current_result.append(1)
                    triangle_layers_data[layer] = current_result

        return list(triangle_layers_data.values())


print(Solution().generate(0))