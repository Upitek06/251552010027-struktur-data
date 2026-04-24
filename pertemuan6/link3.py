class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def hasil_linked_list(node):
    while node:
        next_id = id(node.next) if node.next else None
        print(f"[{node.data}] | {next_id} -> ", end="")
        node = node.next
    print("NULL")

a = Node("Data ke-1")
b = Node("Data ke-2")
c = Node("Data ke-3")

a.next = b
b.next = c

hasil_linked_list(a)