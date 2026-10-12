class Solution(object):
    def countEven(self, num):
        lis=[]
        iseven =[]
        for x in range(2,num+1):
            for i in str(x):
                iseven.append(int(i))
            if sum(iseven)%2==0:
                lis.append(x)
                del iseven[:]
            else:
                del iseven[:]
        return len(lis)
        