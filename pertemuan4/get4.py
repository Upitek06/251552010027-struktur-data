kontak = {'Alvian':'08132456789', 'Rifki':'08234567890'}
print(f"Kontak Alvian: {kontak.get('Alvian')}")
print(F"Nomor yang tidak ada: {kontak.get('Unknowi', 'Kontak tidak ditemukan')}")