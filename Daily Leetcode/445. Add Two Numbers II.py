# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        number1 = ""
        number2 = ""

        temp = l1
        while temp != None:
            number1 += str(temp.val)
            temp = temp.next
            
        temp = l2
        while temp != None:
            number2 += str(temp.val)
            temp = temp.next
        summ = int(number1) + int(number2)
        if summ == 0:
            return l1
        revH = None
        while summ != 0:
            dig = summ % 10
            n = ListNode(dig, revH)
            revH = n
            summ //= 10
        return revH

