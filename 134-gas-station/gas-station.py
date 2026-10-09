class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        ans, curr, total = 0, 0, 0

        for i in range(len(gas)):
            gain = gas[i] - cost[i]
            curr += gain
            total += gain

            if(curr < 0):
                ans = i + 1
                curr = 0

        if total >= 0:
            return ans
        
        return -1