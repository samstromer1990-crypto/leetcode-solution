# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: ListNode | None, left: int, right: int) -> ListNode | None:
        if left > right or not head:
            return head

        def linked_list_to_list(node):
            result = []
            current = node
            while current is not None:
                result.append(current.val)
                current = current.next
            return result

        Lis = linked_list_to_list(head)

        if len(Lis) <= 1 or left == right:
            return head

        Lis[left - 1:right] = reversed(Lis[left - 1:right])

        def list_to_linked_list(lst):
            if not lst:
                return None
            
            new_head = ListNode(lst[0])
            current = new_head
            
            for item in lst[1:]:
                current.next = ListNode(item)
                current = current.next
                
            return new_head

        return list_to_linked_list(Lis)