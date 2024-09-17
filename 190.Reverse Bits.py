class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n: int) -> int:

        return int(bin(n)[2:].zfill(32)[::-1], 2)


test_data_1 = '00000010100101000001111010011100'
print(Solution().reverseBits(test_data_1))
