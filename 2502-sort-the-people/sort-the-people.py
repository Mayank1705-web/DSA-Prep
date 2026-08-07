class Solution(object):
    def sortPeople(self, names, heights):
        """
        :type names: List[str]
        :type heights: List[int]
        :rtype: List[str]
        """
        result = []
        for person in sorted(zip(names, heights), key = lambda x: x[1], reverse = True):
            result.append(person[0])
        
        return result