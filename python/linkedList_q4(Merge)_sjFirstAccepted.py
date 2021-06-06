# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        newL = l1 if l1 else None
        toMergeL = l2 if l2 else None
        if newL and toMergeL:
            if newL.val > toMergeL.val:
                newL,toMergeL = toMergeL, newL    
        elif toMergeL:
            newL,toMergeL = toMergeL, newL
        
        newCur = newL
        toMergeCur = toMergeL
        while newCur:
            cur = newCur
            nxt = newCur.next
            if toMergeCur != None and (nxt == None or toMergeCur.val <= nxt.val):
                cur.next  = toMergeCur
                while toMergeCur :
                    # print("toMergeCur is", toMergeCur.val, "newL nxt is", nxt.val)
                    if nxt == None or toMergeCur.val <= nxt.val:
                        cur = toMergeCur
                        toMergeCur = toMergeCur.next
                        print(newL)
                    else:
                        cur.next = nxt
                        break
            cur.next = nxt
            newCur = nxt
        return newL