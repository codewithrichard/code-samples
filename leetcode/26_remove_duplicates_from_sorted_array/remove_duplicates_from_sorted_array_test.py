import unittest
from ddt import ddt, data, unpack
from typing import List
from remove_duplicates_from_sorted_array import Solution

@ddt
class Tester(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    @data(
        [[1,2,3,4,5], [1,2,3,4,5], 5],
        [[1,1,1,1,1,1,2,2,3,4,4,5], [1,2,3,4,5], 5],
        [[1,1,1,1,1,1,1,1,1,1,2], [1,2], 2],
        [[], [], 0],
        [[1], [1], 1],
    )
    @unpack
    def test(self, nums, nums_after, expected):
        ret = self.s.removeDuplicates(nums)
        self.assertEqual(ret, expected)
        self.assertEqual(nums, nums_after)

if __name__ == '__main__':
    unittest.main()
