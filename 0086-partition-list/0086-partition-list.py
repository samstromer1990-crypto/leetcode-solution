# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: ListNode | None, x: int) -> ListNode | None:
        def linked_list_to_list(head):
            result = []
            current = head
            while current:
                result.append(current.val)
                current = current.next
            return result     
        
        List = linked_list_to_list(head)
        
        def two_group(Lis, X):
            gp1 = []
            gp2 = []
            for i in Lis:
                if i >= X:
                    gp2.append(i)
                else:
                    gp1.append(i)
            return gp1, gp2
        
        Gp1, Gp2 = two_group(List, x)

        def combine(A, B):
            if not A:
                return B
            if not B:
                return A
            else:
                for item in B:
                    A.append(item)
            return A

        def list_to_linked_list(lst):
            if not lst:
                return None
            head = ListNode(lst[0])
            current = head
            for item in lst[1:]:
                current.next = ListNode(item)
                current = current.next
            return head
        
        output = combine(Gp1, Gp2)
        return list_to_linked_list(output)