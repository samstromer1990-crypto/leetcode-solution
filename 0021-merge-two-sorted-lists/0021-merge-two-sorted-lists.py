

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        list_1 = []
        current = list1
        while current is not None:
            list_1.append(current.val)
            current = current.next

        list_2 = []
        current = list2
        while current is not None:
            list_2.append(current.val)
            current = current.next

        listcomm = list_1 + list_2
        listout = sorted(listcomm)

        dummy = ListNode(0)
        current = dummy
        for item in listout:  
            current.next = ListNode(item)
            current = current.next

        return dummy.next