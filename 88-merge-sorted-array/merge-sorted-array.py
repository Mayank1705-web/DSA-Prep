class Solution:
    def merge(self, nums1, m, nums2, n):
        nums1[:] = nums1[:m]      # Keep only first m elements

        for i in range(n):
            nums1.append(nums2[i])

        nums1.sort()