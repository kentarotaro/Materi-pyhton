# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        dumy = ListNode(0)
        current = dumy
        while list1 is not None and list2 is not None:
            if list1.val <= list2.val:
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

        return dumy.next
        
def create_linked_list(arr):
    if not arr:
        return None
    head = ListNode(arr[0])
    current = head
    for val in arr[1:]:
        current.next = ListNode(val)
        current = current.next
    return head

# Fungsi helper untuk mencetak linked list
def print_linked_list(head):
    vals = []
    current = head
    while current:
        vals.append(current.val)
        current = current.next
    print(vals)

# --- Contoh Penggunaan yang Benar ---
x = Solution()

# Buat Linked List dari list Python
list1_nodes = create_linked_list([1, 2, 4])
list2_nodes = create_linked_list([1, 3, 4])
merged_head = x.mergeTwoLists(list1_nodes, list2_nodes)
print("Output Merged Linked List:")
print_linked_list(merged_head)