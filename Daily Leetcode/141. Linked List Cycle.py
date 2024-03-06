# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head == None:
            return False

        temp = head 
        tail = head.next 

        while  tail != None and tail.next != None:
            if tail == temp:
                return True
            temp = temp.next
            tail = tail.next.next
            
        return False
