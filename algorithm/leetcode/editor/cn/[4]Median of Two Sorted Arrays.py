#给定两个大小为 m 和 n 的有序数组 nums1 和 nums2。 
#
# 请你找出这两个有序数组的中位数，并且要求算法的时间复杂度为 O(log(m + n))。 
#
# 你可以假设 nums1 和 nums2 不会同时为空。 
#
# 示例 1: 
#
# nums1 = [1, 3]
#nums2 = [2]
#
#则中位数是 2.0
# 
#
# 示例 2: 
#
# nums1 = [1, 2]
#nums2 = [3, 4]
#
#则中位数是 (2 + 3)/2 = 2.5
# 
# Related Topics 数组 二分查找 分治算法



#leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m = len(nums1)
        n = len(nums2)
        if m == 0:
            return (nums2[n // 2 - 1] + nums2[n // 2]) / 2 if n % 2 == 0 else nums2[n // 2]
        elif n == 0:
            return (nums1[m // 2 - 1] + nums1[m // 2]) / 2 if m % 2 == 0 else nums1[m // 2]

        k = 1
        i = 0
        j = 0
        mid = (m + n) // 2
        left = right = 0
        while k <= mid + 1:
            if nums1[i] < nums2[j] and i < m:
                left = right
                right = nums1[i]
                i += 1
                k += 1

            elif i == m:
                left = right
                right = nums1[i]
                j += 1
                k += 1

            elif nums1[i] >= nums2[j] and j < n:
                left = right
                right = nums1[i]
                j += 1
                k += 1
            elif j == n:
                left = right
                right = nums1[i]
                i += 1
                k += 1

        if (m + n) % 2 == 0:
            return (left + right) / 2
        else:
            return left
        
        
#leetcode submit region end(Prohibit modification and deletion)
