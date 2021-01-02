import unittest
from ddt import ddt, data, unpack
from typing import List
from merge_two_sorted_lists import Solution, ListNode

@ddt
class Tester(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    @data(
        [[], [], []],
        [[1], [], [1]],
        [[1,2,3], [], [1,2,3]],
        [[], [2], [2]],
        [[], [2,3,4], [2,3,4]],
        [[1,2,4], [1,3,4], [1,1,2,3,4,4]],
        [[1,2,4,7,10,10,10], [1,3,4,8,8], [1,1,2,3,4,4,7,8,8,10,10,10]]
    )
    @unpack
    def test(self, l1, l2, expected):
        l1_as_list = self.makeListNode(l1)
        l2_as_list = self.makeListNode(l2)
        ret = self.s.mergeTwoLists(l1_as_list,l2_as_list)
        if ret:
            self.assertEqual(ret.toList(), expected)
        else:
            self.assertEqual([], expected)

    def makeListNode(self, nums: List[int]) -> ListNode:
        if not nums:
            return None
        else:
            return ListNode(nums[0], self.makeListNode(nums[1:]))

if __name__ == '__main__':
    unittest.main()
