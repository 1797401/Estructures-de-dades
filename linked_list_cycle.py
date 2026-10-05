class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def hasCycle(head: ListNode) -> bool:
    nodes_visitats=set()
    while True:
        if head in nodes_visitats:
            return True
        else:
            nodes_visitats.add(head)
            if head:
                head=head.next
            else:
                return False
    
