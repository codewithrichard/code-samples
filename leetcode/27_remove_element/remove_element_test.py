import unittest
from remove_element import Solution
from ddt import ddt, data, unpack

@ddt
class Tester(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    @data(
        [[3,2,2,3], 3, 2],
        [[3,2,2,3], 10, 4],
        [[], 10, 0],
        [[0,1,2,2,3,0,4,2], 2, 5],
    )
    @unpack
    def test(self, nums, val, expected):
        ret = self.s.removeElement(nums,val)
        self.assertEqual(ret, expected)

if __name__ == '__main__':
    unittest.main()
