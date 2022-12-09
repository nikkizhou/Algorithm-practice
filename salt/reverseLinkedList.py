class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def reverseList(self, head):
        if head is None: return head
        newHead=None
        parent = head.next
        child = ListNode(head.val,None)
        while parent is not None:
            # create a new node and connect to the previous created node
            newHead = ListNode(parent.val,child)
            parent = parent.next
            child = newHead
        return newHead

    def reverseListRec(self, head,child):
        if head is None: return child
        next = head.next
        head.next = child
        return self.reverseListRec(next, head)

    def main(self):
      head = ListNode(1,ListNode(2,ListNode(3,ListNode(4,ListNode(5)))))
      result = self.reverseListRec(head)
      while result is not None:
        print(result.val)
        result = result.next


s = Solution()
s.main()
