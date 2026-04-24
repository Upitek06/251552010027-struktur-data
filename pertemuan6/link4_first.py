class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def insert_awal(head, data):
    new_node = Node(data)
    new_node.next = head
    return new_node
    
head = Node("Langkah 2")
head = insert_awal(head, "Langkah 1")

def hasil_linked_list(head):
    while head:
        print(f"[{head.data}] -> ", end="")
        head = head.next
    print("NULL")

hasil_linked_list(head)