class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

a = Node("Langkah 1")
b = Node("Langkah 2")
c = Node("Langkah 3")

a.next = b
b.next = a

current = a
while current:
    print(current.data)
    current = current.next