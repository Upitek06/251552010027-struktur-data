users = {
    'rizwan': 'oranglondon123',
    'nabhan': 'cyber123',
    'hafiz': 'fullstack666'
}

cek_login = [
    ("rizwan", "oranglondon123"),
    ("nabhan", "cyber123"),
    ("hafiz", "fullstack666")
]

for username, password in cek_login:
    if username in users and users[username] == password:
        print(f"Selamat datang, {username}!")
        if username == 'rizwan':
            print("Hai Orang London, ngaret jirr")
    else:
        print(f"Login gagal untuk {username}. Username atau password salah.")