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
