class Node:
    def __init__(self, val, next=None):
        self.value = val
        self.next = next

    def printList(self):
        print(self.value)
        if self.next:
            self.next.printList()

    def add(self, val):
        if not self.next:
            self.next = Node(val)
            return
        self.next.add(val)


A = Node(0)
for i in range(1, 5):
    A.add(i)
A.printList()


def list_reverse(head : Node):
    curr = head
    prev = None
    while 1:
        if not curr:
            return prev
        temp = curr.next
        curr.next = prev
        prev = curr
        curr = temp


print('\n\n\n')
print(list_reverse(A).printList())


# 0: klasdjflkadsj
# 1: kldsafj;lkasd, kjdafl;kasj;lkfdja
# 3: fdlak;jsdfkj, adfj;lkadfjas
# 5: aflj, akdfjl
