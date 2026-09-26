class Solution(object):
    def countSpecialIntegers(self, nums):
        res=0
        dict={}
        for order,values in enumerate(nums):
            if values not in dict:
                dict[values]=[]
            dict[values].append(order)
        for x in dict:
            if len(dict[x])==3 and dict[x][1]-dict[x][0]==dict[x][2]-dict[x][1]:
                res +=1
        return res
        
            