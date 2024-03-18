# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        lst = []
        temp = head
        while temp is not None:
            lst.append(temp.val)
            temp = temp.next
        
        dic = Counter(lst)
        lst = []
        for key, value in dic.items():
            if value < 2:
                lst.append(key)
        dummy = ListNode(None, None)
        tail = dummy
        for i in range(len(lst)):
            n = ListNode(lst[i], None)
            tail.next = n
            tail = n
        return dummy.next
            