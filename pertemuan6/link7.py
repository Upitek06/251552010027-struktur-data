class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def insert_awal(head, data):
    new_node = Node(data)
    new_node.next = head
    return new_node

def insert_akhir(head, data):
    new_node = Node(data)
    if not head:
        return new_node
    current = head
    while current.next:
        current = current.next
    current.next = new_node
    return head

def insert_setelah_node(sebelum, data):
    if not sebelum:
        print("Node sebelumnya tidak boleh None")
        return
    new_node = Node(data)
    new_node.next = sebelum.next
    sebelum.next = new_node

head = Node(" Masuk dari tengah 2")
head = insert_awal(head, "Masuk dari awal 1")
head = insert_akhir(head, "Masuk dari akhir 3")

def hasil_linked_list(head):
    while head:
        print(f"[{head.data}] -> ", end="")
        head = head.next
    print("NULL")
    current = head
    while current and current.data != " Masuk dari tengah 2":
        current = current.next
    insert_setelah_node(current, " Masuk dari tengah 2.5")

hasil_linked_list(head)