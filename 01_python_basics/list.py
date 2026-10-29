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

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = head
        fast = head

        # First step: Determine if there is a cycle
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:  # Cycle detected
                break
        else:
            return None  # No cycle detected

        # Second step: Find the entry point of the cycle
        slow = head
        while slow != fast:
            slow = slow.next
            fast = fast.next

        return slow  # Entry point of the cycle 

class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        dummynode = ListNode(0)
        dummynode.next = head
        current = dummynode

        while current.next:
            if current.next.val == val:
                current.next = current.next.next  # Remove the node
            else:
                current = current.next  # Move to the next node

        return dummynode.next  # Return the new head of the list

class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        # Find the end of the first half and reverse the second half.
        def end_of_first_half(node):
            fast = node
            slow = node
            while fast.next and fast.next.next:
                fast = fast.next.next
                slow = slow.next
            return slow

        def reverse_list(node):
            prev = None
            current = node
            while current:
                next_node = current.next
                current.next = prev
                prev = current
                current = next_node
            return prev

        if not head or not head.next:
            return True

        first_half_end = end_of_first_half(head)
        second_half_start = reverse_list(first_half_end.next)

        # Check whether or not there is a palindrome.
        p1 = head
        p2 = second_half_start
        result = True
        while result and p2:
            if p1.val != p2.val:
                result = False
            p1 = p1.next
            p2 = p2.next

        # Restore the list and return the result.
        first_half_end.next = reverse_list(second_half_start)
        return result

class Solution:
    def removeDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current = head

        while current and current.next:
            if current.val == current.next.val:
                current.next = current.next.next  # Skip the duplicate node
            else:
                current = current.next  # Move to the next node

        return head  # Return the modified list without duplicates

class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummynode = ListNode(0)
        dummynode.next = head
        prev = dummynode
        current = head

        while current:
            # Move current until the end of duplicates
            while current.next and current.val == current.next.val:
                current = current.next

            # If prev's next is still current, no duplicates were found
            if prev.next == current:
                prev = prev.next  # Move prev to next node
            else:
                prev.next = current.next  # Skip all duplicates

            current = current.next  # Move to the next node

        return dummynode.next  # Return the modified list without duplicates

class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        before_head = ListNode(0)  # Dummy node for the 'before' list
        after_head = ListNode(0)   # Dummy node for the 'after' list

        before = before_head  # Pointer to build the 'before' list
        after = after_head    # Pointer to build the 'after' list

        current = head  # Start from the head of the original list

        while current:
            if current.val < x:
                before.next = current  # Add to 'before' list
                before = before.next
            else:
                after.next = current  # Add to 'after' list
                after = after.next
            current = current.next  # Move to the next node

        after.next = None  # Terminate the 'after' list
        before.next = after_head.next  # Connect 'before' and 'after' lists

        return before_head.next  # Return the head of the new partitioned list

class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None

        odd = head  # Pointer for odd indexed nodes
        even = head.next  # Pointer for even indexed nodes
        even_head = even  # Store the head of the even indexed nodes

        while even and even.next:
            odd.next = even.next  # Link odd node to the next odd node
            odd = odd.next  # Move odd pointer to the next odd node
            even.next = odd.next  # Link even node to the next even node
            even = even.next  # Move even pointer to the next even node

        odd.next = even_head  # Connect the end of odd list to the head of even list

        return head  # Return the modified list with odd and even nodes rearranged