from collections import deque

def is_subsequence(a, b):
    queue = deque(a)  # Создаем очередь из символов строки a
    for char in b:
        if not queue:  # Если очередь пуста, все символы найдены
            return True
        if char == queue[0]:
            queue.popleft()  # Удаляем символ из очереди, если он совпадает с текущим символом строки b
    return not queue  # Возвращаем True, если очередь пуста
