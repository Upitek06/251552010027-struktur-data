from collections import deque

queue = deque()

queue.append('Sudais')
queue.append('Hafiz')
queue.append('Nabhan')
print('Queue:', queue)

front = queue[0]
print('Depan:', front)

keluar = queue.popleft()
print('Dequeue:', keluar)
print('Queue: ', queue)

print('Kosong?:', len(queue) == 0)
print('Ukuran:', len(queue))