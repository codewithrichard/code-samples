import unittest
from search_insert_position import Solution
from ddt import ddt, data, unpack

@ddt
class Tester(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    @data(
        [[1,3,5,6], 5, 2],
        [[1,3,5,6], 7, 4],
        [[1,3,5,6], 0, 0],
        [[1,3,5,6], 2, 1],
    )
    @unpack
    def test(self, nums, target, expected):
        ret = self.s.searchInsert(nums,target)
        self.assertEqual(ret, expected)

if __name__ == '__main__':
    unittest.main()
