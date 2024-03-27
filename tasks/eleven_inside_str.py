from collections import deque

def is_subsequence(a, b):
    queue = deque(a)  # очередь из символов строки a
    for char in b:
        if not queue:
            return True
        if char == queue[0]:
            queue.popleft()
    return not queue  # True если очередь пуста
