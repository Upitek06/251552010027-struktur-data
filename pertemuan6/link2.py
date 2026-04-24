class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

a = Node("Nama A")
b = Node("Nama B")
c = Node("Nama C")

a.next = b
b.next = c

current = a
while current:
    print(f"Node @ {id(current)}: {current.data} | Next: {id(current.next) if current.next else None}")
    current = current.next