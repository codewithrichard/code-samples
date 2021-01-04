from typing import List
"""
Given an array nums and a value val, remove all instances 
of that value in-place and return the new length.

Do not allocate extra space for another array, you must 
do this by modifying the input array in-place with O(1) extra memory.

The order of elements can be changed. It doesn't matter what you 
leave beyond the new length.

Input: nums = [3,2,2,3], val = 3
Output: 2, nums = [2,2]

"""
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        
        new_length = 0
        i = 0
        while(True):
            if i >= len(nums):
                break
            else:
                current_num = nums[i]

                if current_num == val:
                    # remove it
                    del nums[i]
                else:
                    # keep it
                    new_length += 1
                    i += 1
        
        return new_length