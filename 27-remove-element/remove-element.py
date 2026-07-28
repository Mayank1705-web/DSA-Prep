class Solution(object):
    def removeElement(self, arr, val):
        j = 0
        for i in range(len(arr)):
            if arr[i] != val:
                arr[i], arr[j] = arr[j], arr[i]
                j += 1
        return j


        