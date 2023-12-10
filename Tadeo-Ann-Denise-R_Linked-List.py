#LAB Problem: Merge Two Sorted Linked List

class ListNode:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next

def merge_sorted_lists(list1, list2):
    dummy = ListNode()
    current = dummy

    while list1 is not None and list2 is not None:
        if list1.value <= list2.value:
            current.next = list1
            list1 = list1.next
        else:
            current.next = list2
            list2 = list2.next

        current = current.next

    if list1 is not None:
        current.next = list1
    elif list2 is not None:
        current.next = list2

    return dummy.next

def print_linked_list(head):
    while head.next:
        print(head.value, end=" -> ")
        head = head.next
    print(head.value)

list1 = ListNode(1, ListNode(2, ListNode(4)))
list2 = ListNode(1, ListNode(3, ListNode(4)))

merged_list = merge_sorted_lists(list1, list2)

print("Merged List:", end=" ")
print_linked_list(merged_list)
