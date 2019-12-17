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
    # Define the function as 'twoSum' and (set arguments as self, given array and target integer)
    def twoSum(self, nums, target):
        
        # Define empty array to variable 'ls'
        ls = []
        # For each integer in array, find length of array from index 0
        for i in range(0, len(nums)):
            # Declare the difference of the target integer and values of the assigned indices in array to variable 'item'
            item = target - nums[i]
            # Declare string "done" to assigned index in array (does it really do anything?)
            nums[i] = "done"                                   # seems to cut runtime on 1/2
            # If the difference of the target integer and values of the assigned indices in array is in given array,..
            if item in nums:
                #... Add the integers in arrat to empty array defined earlier as 'ls'
                ls.append(i)
                #... Add given array indices 
                #  - of the difference of the target integer and assigned index in array 
                #  - to empty array defined earlier as 'ls'
                ls.append(nums.index(item))
                # return the no-longer empty array of indices in which values sum up to be the target integer
                return ls