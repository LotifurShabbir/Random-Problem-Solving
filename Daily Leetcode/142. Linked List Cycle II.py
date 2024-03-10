# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None:
            return None

        temp = head 
        tail = head

        while  tail != None and tail.next != None:
            temp = temp.next
            tail = tail.next.next

            if tail == temp:
                break
        else:
            return None
        
        # print(temp.val)
        # print(tail.val)
                
        temp = head
        while temp != tail:
            temp = temp.next
            tail = tail.next
            
        return temp