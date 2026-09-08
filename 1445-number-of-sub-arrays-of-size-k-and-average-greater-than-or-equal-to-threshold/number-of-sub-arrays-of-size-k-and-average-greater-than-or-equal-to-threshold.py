class Solution(object):
    def numOfSubarrays(self, nums, k, threshold):
        """
        :type arr: List[int]
        :type k: int
        :type threshold: int
        :rtype: int
        """
        s = sum(nums[:k])
        count = int(s >= k * threshold)

        for i in range(k, len(nums)):
            s += nums[i] - nums[i - k]
            count += s >= k * threshold
        
        return count