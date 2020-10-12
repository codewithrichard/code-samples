import unittest
from three_sum import Solution
from ddt import ddt, data, unpack

@ddt
class Tester(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    @data(
        [[-1,0,1,2,-1,-4], [[-1, -1, 2], [-1, 0, 1]]],
        [[],[]],
        [[0],[]],
        [[0,2],[]],
        [[0,1,2],[]],
        [[0,1,2,3,4,5],[]],
        [[0,1,1,-1,-2,5,1,1],[[-2,1,1],[-1,0,1]]],
        [[-3,0,1,1,-1,-2,5,2,1,1],[[-3,-2,5],[-3,1,2],[-2,0,2],[-2,1,1],[-1,0,1]]],
        [[-1,0,1,2,-1,-4,-1,-1,-1,-1,-1,-1,-1,-1], [[-1, -1, 2], [-1, 0, 1]]],
    )
    @unpack
    def test(self, s, expected):
        ret = self.s.threeSum(s)
        self.assertEqual(ret, expected)

if __name__ == '__main__':
    unittest.main()
