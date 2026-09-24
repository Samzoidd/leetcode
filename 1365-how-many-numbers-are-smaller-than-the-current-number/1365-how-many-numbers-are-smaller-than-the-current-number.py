class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        temp=sorted(nums)
        dict={}
        for i, value in enumerate(temp):
            if value not in dict:
                dict[value]=i
        orginal=[]
        for i in nums:
            orginal.append(dict[i])
        return orginal