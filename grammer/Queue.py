# FIFO (First-in ,First-Out)
#      --------------------------
#             -------->>>
#      --------------------------

import queue

data_queue = queue.Queue()

data_queue.put('coding')
data_queue.put(3)

print('QUEUE SIZE : %d' % data_queue.qsize())
print(data_queue.get())
print('QUEUE SIZE : %d' % data_queue.qsize())
print(data_queue.get())

# LIFO (Last-in, First-Out) --> Stack

lifo_queue = queue.LifoQueue()

lifo_queue.put('funcoding')
lifo_queue.put(5)

print('QUEUE SIZE : %d' % lifo_queue.qsize())
print(lifo_queue.get())
print('QUEUE SIZE : %d' % lifo_queue.qsize())
print(lifo_queue.get())

# Priority Queue

prior_queue = queue.PriorityQueue()

# 우선순위가 낮은게 먼저 출력
prior_queue.put((10, 'Korea'))
prior_queue.put((20, 'America'))
prior_queue.put((15, 'China'))

print('QUEUE SIZE : %d' % prior_queue.qsize())
print(prior_queue.get()[1])
print('QUEUE SIZE : %d' % prior_queue.qsize())
print(prior_queue.get()[1])
print('QUEUE SIZE : %d' % prior_queue.qsize())
print(prior_queue.get()[1])

# 연습 1 : 리스트 변수로 큐를 다루는 enqueue, dequeue 기능 구현해보기

queue_list = list()  # 전역변수


def list_enqueue(data):
    queue_list.insert(len(queue_list), data)  # queue_list.append(data)


def list_dequeue():
    if len(queue_list) > 0:
        queue_list.pop(0)


for index in range(1, 10):
    list_enqueue(index)

print(queue_list)
list_dequeue()
print(queue_list)
list_dequeue()
print(queue_list)
list_dequeue()
print(queue_list)
