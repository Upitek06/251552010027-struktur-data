persediaan_barang = []
print(f"Awal: {persediaan_barang}")

persediaan_barang.append('Indomie')
persediaan_barang.append('Kopi GoodDay')
persediaan_barang.append('Gula Pasir')
persediaan_barang.append('Beras')
print(f"Setelah dipush: {persediaan_barang}")


pindahkan_kedepan = persediaan_barang[-1]
print(f"Peek: {pindahkan_kedepan}")

tambahkan = persediaan_barang.pop()
print(f"Dipop: {tambahkan}")

print(f"Stack: {persediaan_barang}")

print(f"Kosong?: {len(persediaan_barang) == 0}")
print(f"Ukuran: {len(persediaan_barang)}")