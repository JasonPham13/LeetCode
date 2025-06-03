class Solution:
    def twoSum(self, nums, target):
        numMap = {}
        for i, num in enumerate(nums):
            diff = target - num
            if diff in numMap:
                return [numMap[diff], i]
            numMap[num] = i
        return []
        

    print(twoSum([2, 7, 11, 15], 9))
