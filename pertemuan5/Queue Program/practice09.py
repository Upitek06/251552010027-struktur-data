from collections import deque

queue = deque()

queue.append('Rizwan')
queue.append('Fajrul')
queue.append('Nabhan')
queue.append('Yahya')
queue.append('Fadil')
deque(['Rizwan', 'Fajrul', 'Nabhan', 'Yahya', 'Fadil'])

print('Antrian Awal:', list(queue))
print('Yang pertama dilayani:', queue[0])
print('--------- Mulai Melayani ---------')

urutan = 1
while queue:
    pelanggan = queue.popleft()
    print(f'[{urutan}] Melayani: {pelanggan}')
    if queue:
        print('Antrian Selanjutnya:', list(queue))
    urutan += 1
print('Semua pelanggan telah dilayani.')