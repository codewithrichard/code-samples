import unittest
from valid_parentheses import Solution
from ddt import ddt, data, unpack

@ddt
class Tester(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    @data(
        ["()", True],
        ["()()()", True],
        ["(){}[]", True],
        ["(){(())}[]", True],
        ["(]", False],
        ["([)]", False],
        ["((((", False],
    )
    @unpack
    def test(self, s, expected):
        ret = self.s.isValid(s)
        self.assertEqual(ret, expected)

if __name__ == '__main__':
    unittest.main()
