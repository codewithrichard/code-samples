import unittest
from ddt import ddt, data, unpack
from typing import List
from merge_k_sorted_lists import Solution, ListNode

@ddt
class Tester(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    @data(
        [ [[]], [] ],
        [ [[1]], [1] ],
        [ [[1],[]], [1] ],
        [ [[1,4,5],[1,3,4],[2,6]],  [1,1,2,3,4,4,5,6] ],
        [ [[1,4,5],[1,3,4],[2,6],[1,2,10,11]],  [1,1,1,2,2,3,4,4,5,6,10,11] ],
    )
    @unpack
    def test(self, input_lists, expected):
        list_of_listnodes = []
        for list in input_lists:
            list_of_listnodes.append(self.makeListNode(list))

        ret = self.s.mergeKLists(list_of_listnodes)
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
