class Solution(object):
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        result = []

        if len(result) == 0:
                result.append(nums[0])

        for i in range(0, len(nums)-1):
            result.append(result[i] + nums[i+1])    
        return result