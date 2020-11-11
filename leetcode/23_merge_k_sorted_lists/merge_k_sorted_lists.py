from typing import List
"""
LeetCode #23 Merge K Sorted Lists

You are given an array of k linked-lists lists, each
linked-list is sorted in ascending order.

Merge all the linked-lists into one sorted linked-list
and return it.

 
Example 1:

Input: lists = [[1,4,5],[1,3,4],[2,6]]
Output: [1,1,2,3,4,4,5,6]
Explanation: The linked-lists are:
[
  1->4->5,
  1->3->4,
  2->6
]
merging them into one sorted list:
1->1->2->3->4->4->5->6

Example 2:

Input: lists = []
Output: []

Example 3:

Input: lists = [[]]
Output: []

 

Constraints:

    k == lists.length
    0 <= k <= 10^4
    0 <= lists[i].length <= 500
    -10^4 <= lists[i][j] <= 10^4
    lists[i] is sorted in ascending order.
    The sum of lists[i].length won't exceed 10^4.

Observations
- can be many lists
- lists are "short"

Strategy
- Merge Sort

[a,b,c]
[d,e,f,a,b,c,d,a,e,d,b,d,e,f]

merge_lists(lists)
    merge first two lists together
    put this new list at the end of the remaining lists
    recursively call merge_lists

ex:
merge_lists([A, B, C, D])
E = merge_two(A, B)
merge_lists([C, D, E])
F = merge_two(C, D)
merge_lists([E, F])
G = merge_two(E, F)
merge_lists([G])
return G

merge_two(list_a, list_b)
    #base cases
    if (list_a is None)
        return list_b
    elif (list_b is None)
        reuturn list_a
    else
        new_node = new ListNode
        new_node.head = smaller of list_a.head and list_b.head
        increment pointer on smaller of list_a or list_b
        new_node.next = recursively call merge_two on new list_a list_b
        return new_node



"""
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def toList(self) -> List[int]:
        if self.next is not None:
            tailList = self.next.toList()
        else:
            tailList = []
        return [self.val] + tailList

class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        #base cases
        if len(lists) == 0:
            return None
        elif len(lists) == 1:
            return lists[0]
        else:
            # merge first two lists together
            mergeList = self.mergeTwo(lists[0], lists[1])

            # put this new list at the end of the remaining lists
            # recursively call merge_lists
            return self.mergeKLists(lists[2:] + [mergeList])

    def mergeTwo(self, a: ListNode, b: ListNode) -> ListNode:
        if not a:
            return b
        elif not b:
            return a
        else:
            # smaller of a or b?
            if a.val < b.val:
                # a is smaller
                head = a
                tail = self.mergeTwo(a.next, b)
            else:
                head = b
                tail = self.mergeTwo(a, b.next)
            head.next = tail
            return head
        """
         
    
        new_node = new ListNode
        new_node.head = smaller of list_a.head and list_b.head
        increment pointer on smaller of list_a or list_b
        new_node.next = recursively call merge_two on new list_a list_b
        return new_node
        """