class Solution:
    def findGCD(self, nums):

        minimum = min(nums)
        maximum = max(nums)

        while minimum != 0:

            maximum, minimum = minimum, maximum % minimum

        return maximum