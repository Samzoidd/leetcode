class Solution:
    def twoSum(self, nums, target):
        dict={}
        for order,value in enumerate(nums):
            find=target-value
            if find in dict:
               return [dict[find],order]
            dict[value]=order
        return