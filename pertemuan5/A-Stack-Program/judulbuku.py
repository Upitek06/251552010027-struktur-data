class Buku_bacaan:
    def __init__(self):
        self.items = []
    
    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        return 'Keranjang Anda Masih Kosong'
    
    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        return 'Tidak ada item yang dapat ditampilkan'
        
    def is_empty(self):
        return len(self.items) == 0
    
    def size(self):
        return len(self.items)
    
    def __str__(self):
        return str(self.items)