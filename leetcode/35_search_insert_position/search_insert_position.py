from typing import List
"""
Given a sorted array of distinct integers and a target value, 
return the index if the target is found. If not, return the 
index where it would be if it were inserted in order.

Recursive binary search
-pick element at middle index
-compare element to target
- element == target
- element is < or > than target

[1,3,5,6], t=5 0 3 (mid_index=1, mid_val=3) (higher)
[1,3,5,6], t=5 1 3 (mid_index=2, mid_val=5) (found!!)

[1,3,5,6], t=7 0 3 (mid_index=1, mid_val=3) (higher)
[1,3,5,6], t=7 1 3 (mid_index=2, mid_val=5) (higher)
[1,3,5,6], t=7 2 3 (mid_index=2, mid_val=5)
                    (special case: lower==mid_index)
                    (t>upper_val, return upper+1)

[1,3,5,6], t=0 0 3 (mid_index=1, mid_val=3) (lower)
[1,3,5,6], t=0 0 1 (mid_index=0, mid_val=1)
                    (special case, lower==mid_index)
                    t<=lower_val, return lower

[1,3,5,6], t=2 0 3 (mid_index=1, mid_val=3) (lower)
[1,3,5,6], t=2 0 1 (mid_index=0, mid_val=1)
                    (special case, lower==mid_index)
                    (t > lower_val and t < upper_val, return upper)

(special case: lower==mid_index)
        t<=lower_val, return lower
        (t < upper_val, return upper)
        (t>upper_val, return upper+1)
        
"""
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        return self.searchInsertRecursive(nums, target, 0, len(nums) - 1)
        
    def searchInsertRecursive(
        self, 
        nums: List[int], 
        target: int,
        lower: int,
        upper: int
        ) -> int:

        if len(nums) == 0:
            return lower
        
        mid_index = (upper + lower) // 2
        mid_val = nums[mid_index]

        if lower == mid_index:
            # Special case
            if target <= nums[lower]:
                return lower
            elif target <= nums[upper]:
                return upper
            else:
                return upper + 1
        
        elif target == mid_val:
            # match
            return mid_index
        elif target < mid_val:
            # lower
            return self.searchInsertRecursive(nums, target, lower, mid_index)
        else:
            # higher
            return self.searchInsertRecursive(nums, target, mid_index, upper)

