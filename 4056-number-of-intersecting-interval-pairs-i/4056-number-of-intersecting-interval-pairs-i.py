class Solution(object):
    def countIntersectingIntervals(self, intervals):  
        res=0
        for i in range(len(intervals)):
            for j in range(i+1,len(intervals)):
                x1,y1=intervals[i]
                x2,y2=intervals[j]
                if max(x1,x2)<=min(y1,y2):
                    res=res+1
        return res

