class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        counter = 0 
        zero_count = 0 
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[counter] = nums[i]
                counter += 1
            else: 
                zero_count += 1 
        if zero_count != len(nums): 
            while counter < len(nums):
                nums[counter] = 0
                counter += 1 
            
            