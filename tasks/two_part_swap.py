def reverse_section(arr, start, end):
    while start < end:
        arr[start], arr[end] = arr[end], arr[start]
        start, end = start + 1, end - 1

def rotate_array(arr, k):
    if not arr:  # Проверка на пустой массив
        return []
    
    n = len(arr)
    k = k % n  # если k больше длины массива
    reverse_section(arr, 0, n-1)
    reverse_section(arr, 0, k-1)
    reverse_section(arr, k, n-1)
    return arr
