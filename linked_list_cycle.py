class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def next_getter(self):
        return self.next


def hasCycle(head: ListNode) -> bool:
    llista=[]
    while True:
        if head in llista:
            return True
        else:
            llista.append(head)
            if head.next:
                head=head.next_getter()
            else:
                return False
    
