class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = list(set(nums))
        nums.sort(reverse = True)
        temp = nums[0]
        for i in range(0, len(nums)):
            if nums[i] <= temp and i < 3 and len(nums) >= 3:
                temp = nums[i]
        return temp
