user = {"name": "Nabhan", "usia": 20, "email":"nabhancyber@gmail.com"}

#Cek email dari user
email = user.get("email", "Email tidak ditemukan")
print(f"Email: {email}")

#Mengupdate data
user.update({"email": "nabhan.updated@gmail.com","role":"cybersecurity"})
print(user)

#Menghapus key
age = user.pop("usia")
print(f"Data setelah pop usia: {user}")

#Menampilkan semua key yang tersedia
print(user.keys())
print(user.values())

#Menyalin dictionary
user_copy = user
print(f"Salinan user: {user_copy}")

print(user)
print(user_copy)