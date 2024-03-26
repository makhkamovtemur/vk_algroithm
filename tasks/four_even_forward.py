def move_evens_forward(arr):
    even_index = 0  # Индекс для вставки следующего четного числа
    for i in range(len(arr)):
        if arr[i] % 2 == 0:
            arr[even_index], arr[i] = arr[i], arr[even_index]
            even_index += 1
    return arr