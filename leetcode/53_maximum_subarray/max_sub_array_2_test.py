import unittest
from max_sub_array_2 import Solution
from ddt import ddt, data, unpack

@ddt
class Tester(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    @data(
        [[1], 1],
        [[-2,1,-3,4,-1,2,1,-5,4], 6],
        [[-2,-1],-1],
        [[0,-1],0]
    )
    @unpack
    def test(self, nums, expected):
        ret = self.s.maxSubArray(nums)
        self.assertEqual(ret, expected)

if __name__ == '__main__':
    unittest.main()
