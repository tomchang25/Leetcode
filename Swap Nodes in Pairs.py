# %%
import copy
from lib.ListNode import ListNode


class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if head is None:
            return None

        if head.next is None:
            return head

        new_head = None
        prev = None
        tag = False
        while 1:
            if ~tag:
                if prev is not None and head.next is not None:
                    prev.next = head.next
                prev = head
            else:
                prev.next = head.next
                head.next = prev

                if new_head is None:
                    new_head = head

            tag = ~tag

            if prev.next is None:
                break
            else:
                head = prev.next

        return new_head


if __name__ == "__main__":

    d = ListNode(4)
    c = ListNode(3, d)
    b = ListNode(2, c)
    a = ListNode(1, b)

    # b = ListNode(2)
    a = ListNode([])

    h = Solution().swapPairs(a)
    print(h)
# %%
