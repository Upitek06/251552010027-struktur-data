class Belanjaan:
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
    
def main():
    Keranjang = Belanjaan()
    Keranjang.push('Sabun')
    Keranjang.push('Pepsodent')
    Keranjang.push('Kecap')
    
    print("Item yang ditambahkan kedalam keranjang:", Keranjang)

    print("Item yang dihapus:", Keranjang.pop())

    print("Item terakhir:", Keranjang.peek())

    print("Apakah keranjang kosong?", Keranjang.is_empty())

    print("Jumlah item dalam keranjang:", Keranjang.size())

    print("Isi stack:", Keranjang)

main()