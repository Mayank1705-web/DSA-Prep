class Solution(object):
    def sortPeople(self, names, heights):
        """
        :type names: List[str]
        :type heights: List[int]
        :rtype: List[str]
        """
        result = []
        for person in sorted(zip(names, heights), key = lambda x: x[1], reverse = True):
            name = person[0]
            result.append(name)
        
        return result