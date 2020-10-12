from typing import List, Dict, Tuple, Set
class Solution:

    """
    Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0? 
    Find all unique triplets in the array which gives the sum of zero.

    Notice that the solution set must not contain duplicate triplets.

    Example input [-1,0,1,2,-1,-4]
    Output: [[-1,-1,2],[-1,0,1]]

    input: [-1,0,1,2,-1,-4,-1,-1,-1,-1]

    Thoughts/Notes:
    1) No duplicates means that any number that exists > 3 times can be removed
    [0, 0, 0], [-1,-1, 2]

    2) A + B + C = 0
    A + B = -C
    C = -A - B

    Dictionary[number_in_nums:int, indexes:List[int]]
    input: [-1,0,1,2,-1,-4]
    dict: {-1:[0, 4], 0:[1], 1:[2], 2:[3], -4:[5]}

    input: [-1,0,1,2,-4]
    dict: {-1:[0], 0:[1], 1:[2], 2:[3], -4:[4]}
    A=-1
    B=2
    Looking for C = -1

    for every element in nums:      # A
        for every element in nums:  # B
            Does -(A+B) exist in dict? 
    """



    def threeSum(self, nums: List[int]) -> List[List[int]]: 
        if len(nums) < 3:
            return []
        
        # 1) No duplicates means that any number that exists > 3 times can be removed
        # At most 3 copies of any number
        nums = self.reduce_nums(nums)
        
        # Create out dictionary
        # Dictionary[number_in_nums:int, indexes:List[int]]
        num_to_index_dict = self.create_indexes(nums)

        # search combinations of A+B ?= -C
        # build our output (order the output)

        # Set[Tuple[int,int,int]]
        set_of_triplets = set()
        for i in range(0, len(nums) - 1):
            for j in range(i + 1, len(nums)):
                a = nums[i]
                b = nums[j]
                # C = -a-b

                if -(a+b) in num_to_index_dict:
                    # possible matches, value is List[int]
                    possible_indexes = num_to_index_dict.get(-a-b)
                    # any index is valid?
                    for k in possible_indexes:
                        if k != i and k != j:
                            # yay, we found unique indexes where A+B+C=0
                            list_of_nums = [a, b, -a-b]
                            list_of_nums.sort()
                            set_of_triplets.add((list_of_nums[0], list_of_nums[1], list_of_nums[2]))
        
        # convert Tuples to Lists
        # Set[Tuple[int,int,int]]
        output = []
        for triplet in set_of_triplets:
            list_of_nums = [triplet[0], triplet[1], triplet[2]]
            output.append(list_of_nums)

        output.sort()
        return output


        
    # At most 3 copies of any number    
    def reduce_nums(self, nums: List[int]) -> List[int]:
        nums_count = {} #Dict[number:int, count:int]
        for num in nums:
            if num in nums_count:
                nums_count[num] = nums_count[num] + 1
            else:
                nums_count[num] = 1

        # rebuild nums
        reduced_nums = []
        for num in nums_count.keys():
            num_count = nums_count[num]
            for i in range(0, min(num_count, 3)):
                reduced_nums.append(num)
        
        return reduced_nums


        
    # Dictionary[number_in_nums:int, indexes:List[int]]
    def create_indexes(self, nums: List[int]) -> Dict[int, List[int]]:
        num_to_index_dict = {}
        for i in range(0, len(nums)):
            cur_num = nums[i]
            if cur_num in num_to_index_dict:
                cur_indexes = num_to_index_dict[cur_num] #List[int]
                cur_indexes.append(i)
                num_to_index_dict[cur_num] = cur_indexes
            else:
                num_to_index_dict[cur_num] = [i]
        
        return num_to_index_dict