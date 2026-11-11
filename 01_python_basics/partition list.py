# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# class Solution(object):
#     def partition(self, head, x):
#         """
#         :type head: Optional[ListNode]
#         :type x: int
#         :rtype: Optional[ListNode]
#         """

class Solution(object):
    def partition(self, head, x):
        
        # create 2 dummy nodes
        before = ListNode(0)
        after = ListNode(0)

        # create 2 tail pointers
        before_tail = before
        after_tail = after

        # current pointer
        current = head

        while current is not None:

            if current.val < x:
                before_tail.next = current
                before_tail = before_tail.next

            else:
                after_tail.next = current
                after_tail = after_tail.next

            current = current.next

        # end the after list
        after_tail.next = None

        # connect both lists
        before_tail.next = after.next

        return before.next


#      #create 2 dummy nodes
#      	#before=smaller than x
#       #after= greater than x or =
      
#       #create 2 tail pointers
#       	before tail=before
#         after tail=after
        
#       #set current=head
      
#       #while current is not none
#       	#if
#         #else
        
#       #piece it together
      
#       [1,4,3,2,5,2] x=3
      
#       before <3
#       afrer >=3
#       before=ListNode(0)
#       after=LN(0)
      
#       [dummy]
#       [dummy]
      
#       #the last poistion in the list
#       beforetail=before
#       aftertail=after
      
#       #traverse the orignal
#       current=head
      
#       while current
#       	if current.val <x:
#         	soemthing else
#           beforetail.next=current
#           beforetail=beforetail.next
#         else:
#         	aftertail.next=current
#           aftetail=aftertail.next
#         current=current.next
        
#         #conect the 2 list
#         #terminatetheafter list
#         #return
        
        
        
        
      
#     before=listnode(0_
#     beforetail=before
    
#        BeforeTail(2)
#     0->none
      
      
      
      
      
#       class Solution(object):
#     def partition(self, head, x):
#         """
#         :type head: Optional[ListNode]
#         :type x: int
#         :rtype: Optional[ListNode]
#         ""
#         before=ListNode(0)
#         after=ListNode(0)
#         beforetail = before
#         aftertail = after
#       	current = head
        
#         while current:
#         	if current.val < x:
#           	beforetail.next = current
#             beforetail = beforetail.next
#           else:
#           	aftertail.next = current
#             aftertail = aftertail.next
#           current = current.next
        
#         beforetail.next = aftertail
#         aftertail.next = None
        
#         return before.next