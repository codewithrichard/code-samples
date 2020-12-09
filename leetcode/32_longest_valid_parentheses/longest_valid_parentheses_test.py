import unittest
from ddt import ddt, data, unpack
from typing import List
from longest_valid_parentheses import Solution

@ddt
class Tester(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    @data(
        ["", 0],
        ["()", 2],
        ["(())", 4],
        ["(()())", 6],
        [")()())", 4],
        [")()()(()))", 8],
        ["())()", 2],
        ["()(()", 2],
    )
    @unpack
    def test(self, s, expected):
        ret = self.s.longestValidParentheses(s)
        self.assertEqual(ret, expected)

if __name__ == '__main__':
    unittest.main()
