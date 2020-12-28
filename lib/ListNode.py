class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        if self.next is None:
            return str(self.val)
        else:
            return str(self.val) + " , " + str(self.next)
