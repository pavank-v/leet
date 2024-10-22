# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(
        self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        node = ListNode()
        val1 = ""
        val2 = ""
        while l1:
            val1 += str(l1.val)
            l1 = l1.next
        while l2:
            val2 += str(l2.val)
            l2 = l2.next
        ans = str(int(str(val1[::-1])) + int(str(val2[::-1])))
        print(ans)
        node = ListNode()
        curr = node

        while ans:
            curr.next = ListNode(int(ans[-1]))
            ans = ans[:-1]
            curr = curr.next
        return node.next
