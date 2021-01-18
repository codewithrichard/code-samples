from typing import List
"""
Given an integer array nums, find the contiguous subarray 
(containing at least one number) which has the largest 
sum and return its sum.

[-2,1,-3,4,-1,2,1,-5,4] => 6

[6,-3,4,...] total=0 (positive, add to running total)
 ^
[6,-3,4,...] total=6 (neg, add to running total iff total > 0)
    ^
[6,-3,4,...] total=3 (positive, add to running total) 
      ^

[2,-3,4,....] total =0
 ^
[2,-3,4,....] total =2 (negative)
    ^
[2,-3,4,....] total = -1 ()
      ^
"""

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        running_total = 0
        best_sum = None

        for num in nums:
            # check individual numbers. It could be the best
            if best_sum is None or num > best_sum:
                best_sum = num

            if num > 0:
                #positive
                if running_total > 0:
                    running_total += num
                else:
                    running_total = num

            else:
                #negative
                running_total += num
      
            # maybe update best_sum
            if running_total > best_sum and running_total > 0:
                best_sum = running_total
        return best_sum