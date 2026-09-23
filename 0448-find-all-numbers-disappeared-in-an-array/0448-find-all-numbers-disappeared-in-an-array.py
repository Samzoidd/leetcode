class Solution(object):
    def findDisappearedNumbers(self, nums):
        sets=set(nums)
        ret=[]
        for i in range(1,len(nums)+1):
            if i not in sets:
                ret.append(i)
        return(ret)
        