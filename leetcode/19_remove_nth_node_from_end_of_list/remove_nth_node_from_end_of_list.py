from typing import List

"""
Given the head of a linked list, remove the nth node from the end of the list and return its head.

Example 1:

Input: head = [1,2,3,4,5], n = 2
Output: [1,2,3,5]

Example 2:

Input: head = [1], n = 1
Output: []

Example 3:

Input: head = [1,2], n = 1
Output: [1]

Case 1: Remove nth node (not the first node)
n=1, target node to remove (3)
(1)->(2)->(3)-> n=1, tb=0 (tb=trailing_by)
HTI

H = head
T = trailing_node
I = incrementing_node

(1)->(2)->(3)-> n=1, tb=1
HT    I
n==tb and I.next is not None, continue progress I and T

(1)->(2)->(3)-> n=1, tb=1
H     T    I
n==tb and I.next is None. set t.next=t.next.next, returns (1)->(2)->


n=2, target to remove (2)
(1)->(2)->(3)-> n=2, tb=0
HTI

(1)->(2)->(3)-> n=2, tb=1
HT    I

(1)->(2)->(3)-> n=2, tb=2
HT         I
n==tb and I.next is None, set t.next=t.next.next, returns (1)->(3)->


Case 2: Remove 1st node
n=1, target to remove (1)
(1)-> n=1 tb=0
HTI
if I.next is None and n-tb==1, remove 1st node, return h.next (None)


n=2, target to remove (1)
(1)->(2)->  n=2, tb=0
HTI

(1)->(2)->  n=2, tb=1
HT    I
i.next is None and n-tb==1, remove 1st node, return h.next (2)->



Case 3: Invalid node to remove
n=10
(1)-> n=10, tb=0
HTI
i.next is None and n-tb > 1, return head (don't remove any nodes)

"""

# Definition for singly-linked list.
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

    def __str__(self):
        if self.val is None:
            return "None"
        else:
            return str(self.val)

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        if head is None:
            return head
        
        trailing_by = 0
        incrementing_node = head
        trailing_node = head

        # increment incrementing_node until trailing_by == n
        while trailing_by < n:
            # Can I increment?
            if incrementing_node.next:
                # yes, safe to increment
                incrementing_node = incrementing_node.next
                trailing_by += 1
            else:
                # can't increment, hit end of list
                if n - trailing_by == 1:
                    # remove 1st node
                    return head.next
                else:
                    #can't remove any nodes, n is too high
                    return head
        
        # we know trailing_by == n
        # increment both incrementing_node and trailing_node until we hit end of list
        while incrementing_node.next:
            incrementing_node = incrementing_node.next
            trailing_node = trailing_node.next

        # at end of list
        # remove the nth node
        trailing_node.next = trailing_node.next.next
        return head
        