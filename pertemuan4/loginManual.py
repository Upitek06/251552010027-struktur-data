users = {
    'rizwan': 'oranglondon123',
    'nabhan': 'cyber123',
    'hafiz': 'fullstack666'
}

print("=========Halaman Login=========")
username = str(input("Masukkan username: "))
password = str(input("Masukkan password: "))

if username in users and users[username] == password:
    print(f"Selamat datang, {username}!")
    if username == 'rizwan':
        print("Hai Orang London, ngaret jirr")
else:
    print("Username atau password salah. Silakan coba lagi.")