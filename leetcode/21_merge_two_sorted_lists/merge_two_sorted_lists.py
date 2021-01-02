from typing import List
"""
Merge two sorted linked lists and return it as a 
sorted list. The list should be made by 
splicing together the nodes of the first two lists.

Input: l1 = [1,2,4], l2 = [1,3,4]
Output: [1,1,2,3,4,4]

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
    
    def __str__(self) -> str:
        return str(self.val)
    
"""
Loop, each iteration:
- base cases l1 = [], l2= []
- identify lowest node, l1.val or l2.val
- append lowest node to output
- "pop" lowest node off of its list
  (increment pointer of l1 or l2 (lowest))
"""

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        
        head = None
        tail = None

        while l1 or l2:
            # lowest node
            nextNode, l1, l2 = self.getLowestNode(l1, l2)

            # append next node to output list
            if not head:
                # first node
                head = nextNode
                tail = nextNode
            else:
                # subsequent nodes
                tail.next = nextNode
                tail = nextNode
        return head

    def getLowestNode(self, l1: ListNode, l2: ListNode) -> ListNode:
        if not l1 and not l2:
            return None
        elif not l1:
            lower = l2
            l2 = None
        elif not l2:
            lower = l1
            l1 = None
        elif l1.val < l2.val:
            lower = l1
            l1 = l1.next
        else:
            lower = l2
            l2 = l2.next
        return lower, l1, l2