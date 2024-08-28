class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        nums1_cur_index = 0
        nums1_tail_value = nums1[m-1]
        if m == 0:
            for index in range(n):
                nums1[index] = nums2[index]

        while nums1_cur_index < len(nums1) and nums2 and m != 0 and nums1_tail_value > nums2[0]:
            current_nums1_elem = nums1[nums1_cur_index]
            current_nums2_elem = nums2[0]
            previous_num1_elem = nums1[nums1_cur_index - 1]
            if current_nums1_elem > current_nums2_elem:
                for elem in reversed(range(nums1_cur_index, m)):
                    nums1[elem + 1] = nums1[elem]
                nums1[nums1_cur_index] = nums2[0]
                del nums2[0]
                n -= 1
                m += 1
            elif current_nums1_elem < previous_num1_elem and nums1_cur_index != 0:
                nums1[nums1_cur_index] = nums2[0]
                del nums2[0]
                n -= 1
            nums1_cur_index += 1
        nums1_cur_index += 1
        if nums2:
            if nums1_tail_value <= nums2[0] and nums2:
                while n != 0:
                    current_nums2_elem = nums2[0]
                    nums1[m] = current_nums2_elem
                    del nums2[0]
                    nums1_cur_index += 1
                    n -= 1
                    m += 1

        return nums1



test_data_1_nums1 = [1, 2, 3, 0, 0, 0]
test_data_1_m = 3
test_data_1_nums2 = [2, 5, 6]
test_data_1_n = 3

test_data_3_nums1 = [0]
test_data_3_m = 0
test_data_3_nums2 = [1]
test_data_3_n = 1

test_data_4_nums1 = [4, 5, 6, 0, 0, 0]
test_data_4_m = 3
test_data_4_nums2 = [1, 2, 3]
test_data_4_n = 3

test_data_5_nums1 = [-1, 0, 0, 3, 3, 3, 0, 0, 0]
test_data_5_m = 6
test_data_5_nums2 = [1, 2, 2]
test_data_5_n = 3

test_data_6_nums1 = [-12,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
test_data_6_m = 1
test_data_6_nums2 = [-49,-45,-42,-41,-40,-39,-39,-39,-38,-36,-34,-34,-33,-33,-32,-31,-29,-28,-26,-26,-24,-21,-20,-20,-18,-16,-16,-14,-11,-7,-6,-5,-4,-4,-3,-3,-2,-2,-1,0,0,0,2,2,6,7,7,8,10,10,13,13,15,15,16,17,17,19,19,20,20,20,21,21,22,22,24,24,25,26,27,29,30,30,30,35,36,36,36,37,39,40,41,42,45,46,46,46,47,48]
# test_data_6_nums2 = [-14,-11,-7,-6,-5,-4,-4,-3,-3,-2,-2,-1,0,0,0,2,2,6,7,7,8,10,10,13,13,15,15,16,17,17,19,19,20,20,20,21,21,22,22,24,24,25,26,27,29,30,30,30,35,36,36,36,37,39,40,41,42,45,46,46,46,47,48]
test_data_6_n = 90
# test_data_6_n = 63

test_data_7_nums1 = [0,0,3,0,0,0,0,0,0]
test_data_7_m = 3
test_data_7_nums2 = [-1,1,1,1,2,3]
test_data_7_n = 6

print(Solution().merge(
    test_data_1_nums1, test_data_1_m, test_data_1_nums2, test_data_1_n))
print(Solution().merge(
    test_data_3_nums1, test_data_3_m, test_data_3_nums2, test_data_3_n))
print(Solution().merge(
    test_data_4_nums1, test_data_4_m, test_data_4_nums2, test_data_4_n))
print(Solution().merge(
    test_data_5_nums1, test_data_5_m, test_data_5_nums2, test_data_5_n))
print(Solution().merge(
    test_data_6_nums1, test_data_6_m, test_data_6_nums2, test_data_6_n))
print(Solution().merge(
    test_data_7_nums1, test_data_7_m, test_data_7_nums2, test_data_7_n))

# Only need to modify nums1 and return nothing!