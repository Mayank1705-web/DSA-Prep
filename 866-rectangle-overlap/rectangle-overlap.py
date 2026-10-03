# class Solution(object):
#     def side_length(self, x1, y1, x2, y2):
#         return (((x2 - x1)**2) + ((y2 - y1)**2))**0.5
#     def isRectangleOverlap(self, rec1, rec2):
#         l1 = self.side_length(rec1[0], rec1[1], rec1[2], rec1[3])
#         b1 = self.side_length(rec1[0], rec1[1], rec1[2], rec1[3])
#         l2 = self.side_length(rec2[0], rec2[1], rec2[2], rec2[3])
#         b2 = self.side_length(rec2[0], rec2[1], rec2[2], rec2[3])

#         if (l1 * b1) == (l2 * b2):
#             return True
        
#         return False\


class Solution:

    def isRectangleOverlap(self, rec1, rec2):

        if rec2[0] >= rec1[2]:
            return False

        if rec2[1] >= rec1[3]:
            return False

        if rec2[2] <= rec1[0]:
            return False

        if rec2[3] <= rec1[1]:
            return False

        return True