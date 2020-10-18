from typing import List

"""
Strategy
* In place single traversal
* maintain a most_recent
* index pointer to current element
* remove duplicate element in place
* increment a counter when see a new unique number


EXAMPLE 1
input nums=[1,1,2], output=2 and nums=[1,2]


c=0,input nums=[1,1,2] # grab first element as most_recent 
                         increment counter and pointer

c=1, most_recent=1, nums=[1,1,2] # found dupe, remove it
                            ^      delete element, keep pointer

c=1,most_recent=1, nums=[1,2] # found new number
                           ^    increment counter and pointer

c=2, most_recent=2, nums=[1,2]
                              ^ #done



EXAMPLE 2
input nums=[1,2,2,3], output=3 and nums=[1,2,3]

c=0, input_nums=[1,2,2,3] # grab first element as most_recent
                            increment counter and pointer

c=1, most_recent=1, nums=[1,2,2,3]  #found new number
                            ^        increment counter and pointer

c=2, most_recent=2, nums=[1,2,2,3]  # found dupe, remove it
                              ^       delete element, keep pointer

c=2, most_recent=2, nums=[1,2,3]    # found new number
                              ^       increment counter and pointer

c=3, most_recent=3, nums=[1,2,3]    # done
                                ^       

EXAMPLE 3
input nums = [], output=0, nums= []

"""

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        else:
            return 1 + self.remove_dupes(nums, nums[0], 1)        

    def remove_dupes(self, nums: List[int], most_recent: int, position: int) -> int:
        if position >= len(nums):
            return 0
        else:
            if most_recent == nums[position]:
                # Found a duplicate, remove it
                del nums[position]

                # recurse, position stays the same since we deleted an item
                return self.remove_dupes(nums, most_recent, position)

            else:
                # Found a new number
                return 1 + self.remove_dupes(nums, nums[position], position + 1)
