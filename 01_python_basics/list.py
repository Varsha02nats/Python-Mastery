# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carryover=0
        dummynode = ListNode(0)
        current = dummynode

        #iterate through the linked lists
        while l1 or l2 or carryover:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0

            sum = val1 + val2 + carryover
            carryover = sum // 10
            digit = sum%10

            current.next = ListNode(digit)
            current = current.next

            if l1:
                l1= l1.next
            if l2:
                l2 = l2.next

        return dummynode.next

class Solution:
    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummynode = ListNode(0)
        current = dummynode

        while l1 and l2:
            if l1.val < l2.val:
                current.next = l1
                l1 = l1.next
            else:
                current.next = l2
                l2 = l2.next
            current = current.next

        # If there are remaining nodes in either list, append them
        if l1:
            current.next = l1
        elif l2:
            current.next = l2

        return dummynode.next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummynode = ListNode(0)
        dummynode.next = head
        first = dummynode
        second = dummynode

        # Move first pointer n+1 steps ahead
        for _ in range(n + 1):
            first = first.next

        # Move both pointers until first reaches the end
        while first:
            first = first.next
            second = second.next

        # Remove the nth node from the end
        second.next = second.next.next

        return dummynode.next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        current = head

        while current:
            next_node = current.next  # Store the next node
            current.next = prev       # Reverse the link
            prev = current            # Move prev to current
            current = next_node       # Move to the next node

        return prev  # New head of the reversed list

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next          # Move slow pointer by 1
            fast = fast.next.next     # Move fast pointer by 2

            if slow == fast:          # Cycle detected
                return True

        return False  # No cycle detected

