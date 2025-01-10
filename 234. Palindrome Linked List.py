"""
234. Palindrome Linked List
https://leetcode.com/problems/palindrome-linked-list/
"""
'''class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        def get_node_at_index(head, index):
            current = head
            for _ in range(index):
                current = current.next
            return current

        length = 0
        current = head
        while current:
            length += 1
            current = current.next

        for i in range(length // 2):
            start_node = get_node_at_index(head, i)
            end_node = get_node_at_index(head, length - i - 1)
            if start_node.val != end_node.val:
                return False

        return True

def list_to_linked_list(elements):
    if not elements:
        return None
    head = ListNode(elements[0])
    current = head
    for value in elements[1:]:
        current.next = ListNode(value)
        current = current.next
    return head
'''
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        if not head or not head.next:
            return True

        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        prev = None
        while slow:
            temp = slow.next
            slow.next = prev
            prev = slow
            slow = temp

        first_half, second_half = head, prev
        while second_half:
            if first_half.val != second_half.val:
                return False
            first_half = first_half.next
            second_half = second_half.next

        return True

def list_to_linked_list(elements):
    if not elements:
        return None
    head = ListNode(elements[0])
    current = head
    for value in elements[1:]:
        current.next = ListNode(value)
        current = current.next
    return head



solution = Solution()
print(solution.isPalindrome(list_to_linked_list([1, 2, 2, 1])))
print(solution.isPalindrome(list_to_linked_list([1, 2])))