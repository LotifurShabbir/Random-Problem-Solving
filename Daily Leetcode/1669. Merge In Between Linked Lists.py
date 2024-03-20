# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        temp = list1
        cnt = 0
        while temp != None:
            if cnt == a - 1:
                break
            cnt += 1
            temp = temp.next
        
        temp2 = temp
        cnt2 = cnt
        while temp2 != None:
            if cnt2 == b + 1:
                break
            cnt2 += 1
            temp2 = temp2.next
        temp.next = list2
        
        last = list2
        while last.next != None:
            last = last.next
        last.next = temp2

        return list1