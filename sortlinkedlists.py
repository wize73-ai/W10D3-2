class Solution(object):
    def mergeTwoLists(self, list1, list2):
        # a new head node for linked list output
        newHead = ListNode()
        current = newHead

        # select lower value of two options and add to new list updating head
        while list1 and list2:
            if list1.val <= list2.val:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next
            current = current.next

        # add orphaned list items when only one list remaining
        current.next = list1 if list1 else list2

        # Return the merged list, starting from newHead(new node for merged list)
        return newHead.next

    def create_linked_list(self, lst):
        if not lst:
            return None
        head = ListNode(lst[0])
        current = head
        for value in lst[1:]:
            current.next = ListNode(value)
            current = current.next
        return head

    def print_linked_list(self, node):
        values = []
        while node:
            values.append(node.val)
            node = node.next
        print(" -> ".join(map(str, values)) + " -> None")
