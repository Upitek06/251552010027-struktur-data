import time

class Node:

    def __init__(self, data):
        self.data = data
        self.next = None

def insert_akhir(head, data):
    new_node = Node(data)
    if not head:
        return new_node
    current = head
    while current.next:
        current = current.next
    current.next = new_node
    return head
    
head = Node("Langkah 2")
head = insert_akhir(head, "Langkah 3")

def hasil_linked_list(head):
    while head:
        print(f"{time.sleep(2)}[{head.data}] {time.sleep(2)}-> ", end="")
        head = head.next
    time.sleep(2)
    print("NULL")

hasil_linked_list(head)