#Solution 1
# class Solution:
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
#         r = [2,7,11,15]

#         for i in range(len(nums)):
#             temp = target - nums[i]
#             if temp in r:
#                 return [i,nums.index(temp)]

#             r.append(nums[i])    



# Solution 2
class Solution:
    def twoSum(self, nums, target):
        ls = []
        for i in range(0, len(nums)):
            item = target - nums[i]
            nums[i] = "done"
            if item in nums:
                ls.append(i)
                ls.append(nums.index(item))
                return ls