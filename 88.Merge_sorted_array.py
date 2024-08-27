class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        result = []
        nums1 = nums1[:m]
        nums2 = nums2[:n]
        if not nums1:
            result = nums2
        elif not nums2:
            result = nums1
        else:
            while nums1 or nums2:
                if nums1 and nums2:
                    if nums1[0] > nums2[0]:
                        result.append(nums2[0])
                        del nums2[0]
                    elif nums2[0] >= nums1[0]:
                        result.append(nums1[0])
                        del nums1[0]
                elif nums1 and not nums2:
                    result.append(nums1[0])
                    del nums1[0]
                elif nums2 and not nums1:
                    result.append(nums2[0])
                    del nums2[0]
        return result


test_data_1_nums1 = [1,2,3,0,0,0]
test_data_1_m = 3
test_data_1_nums2 = [2,5,6]
test_data_1_n = 3

test_data_3_nums1 = [0]
test_data_3_m = 1
test_data_3_nums2 = [1]
test_data_3_n = 1

print(Solution().merge(test_data_1_nums1, test_data_1_m, test_data_1_nums2, test_data_1_n))
print(Solution().merge(test_data_3_nums1, test_data_3_m, test_data_3_nums2, test_data_3_n))
