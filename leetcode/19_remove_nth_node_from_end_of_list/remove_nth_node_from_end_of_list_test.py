import unittest
from ddt import ddt, data, unpack
from typing import List
from remove_nth_node_from_end_of_list import Solution, ListNode

@ddt
class Tester(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    @data(
        [[1,2,3,4,5], 1, [1,2,3,4]],
        [[1,2,3,4,5], 2, [1,2,3,5]],
        [[1,2,3,4,5], 3, [1,2,4,5]],
        [[1,2,3,4,5], 4, [1,3,4,5]],
        [[1,2,3,4,5], 5, [2,3,4,5]],
        [[1,2,3], 3, [2,3]],
        [[1], 1, []],
        [[1], 10, [1]],
        [[1,2,3], 10, [1,2,3]],
    )
    @unpack
    def test(self, nums, n, expected):
        head = self.makeListNode(nums)
        ret = self.s.removeNthFromEnd(head,n)
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
