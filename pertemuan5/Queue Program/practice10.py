import heapq

prioritas = []

heapq.heappush(prioritas, (3, 'Tugas 1'))
heapq.heappush(prioritas, (1, 'Tugas 2'))
heapq.heappush(prioritas, (2, 'Tugas 3'))

print('Prioritas Awal:', prioritas)

while prioritas:
    pq, task = heapq.heappop(prioritas)
    print(f' Prioritas {pq} Proses: {task}')
    