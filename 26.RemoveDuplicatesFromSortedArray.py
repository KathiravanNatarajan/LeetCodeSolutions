class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        counter = 0
        for i in range(len(nums)):
            if i == 0: 
                list_element = nums[i]
            if i>0:
                if list_element != nums[i]:
                    list_element = nums[i]
                    counter += 1 
                    nums[counter] = nums[i]
                else: 
                    continue
        return counter+1
        # return len(list(set(nums))) - Easy python solution but not O(1)
        