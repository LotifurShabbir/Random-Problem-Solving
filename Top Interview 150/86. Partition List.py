# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        first = ListNode(0)
        first_tail = first

        second = ListNode(0)
        second_tail = second

        temp = head
        
        while temp != None:
            if temp.val < x:
                n = ListNode(temp.val)
                first_tail.next = n
                first_tail = n
                
            else:
                n = ListNode(temp.val)
                second_tail.next = n
                second_tail = n

            temp = temp.next
        temp = first
        while temp.next != None:
            temp = temp.next
        temp.next = second.next
        
        return first.next