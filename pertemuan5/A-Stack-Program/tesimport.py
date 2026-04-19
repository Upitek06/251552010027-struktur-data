from judulbuku import Buku_bacaan

Book = Buku_bacaan()
Book.push('Cara Ternak Lele untuk Lulusan IT Tahun 2028/2029')
Book.push('Ingin Menjadi Programmer Handal, Namun Enggan Mengoding')
Book.push('Khusus Lulusan IT! 10 Alasan kenapa kamu harus menjadi peternak lele')

print('Buku yang telah dibaca: ', Book.pop())
print('Buku selanjutnya yang akan dibaca: ', Book.peek())
print('Apakah buku sudah habis? ', Book.is_empty())
print('Jumlah buku yang belum dibaca: ', Book.size())
