# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: ListNode | None, left: int, right: int) -> ListNode | None:

        if left > right:
            return head

        def linked_list_to_list(head):
            result = []
            current = head
            while current is not None:
                result.append(current.val)
                current = current.next
            return result

        Lis = linked_list_to_list(head)

        if len(Lis) == 0:
            return head 

        def swap_with_more(Lis):
            for i in range(len(Lis)):
                if 0 < i < len(Lis) - 1:
                    if i - 1 == left - 1 and i + 1 == right - 1:
                        Lis[i-1], Lis[i+1] = Lis[i+1], Lis[i-1] 
                        break
                    else:
                        continue
                else:
                    sub = Lis[left - 1:right]
                    sub.reverse()
                    Lis[left - 1:right] = sub
                    break
            return Lis
        
        def swap_with_less(Lis):
            if len(Lis) >= 2:
                Lis[0], Lis[1] = Lis[1], Lis[0]
            return Lis

        if len(Lis) == 1:
            Output = swap_with_less(Lis)
        else:
            Output = swap_with_more(Lis)

        def list_to_linked_list(lst):
            if not lst:
                return None
            
            new_head = ListNode(lst[0])
            current = new_head
            
            for item in lst[1:]:
                current.next = ListNode(item)
                current = current.next
                
            return new_head

        output = list_to_linked_list(Output)

        return output