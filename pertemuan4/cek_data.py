inventory = {
    'laptop': 10,
    'mouse': 25,
    'keyboard': 15
}

print("Menambahkan monitor ke inventory")
inventory['monitor'] = 5
print(f"Inventory saat ini: {inventory}")

print("Laptop terjual 2 unit")
inventory['laptop'] -= 2
print(f"Inventory setelah penjualan: {inventory}")