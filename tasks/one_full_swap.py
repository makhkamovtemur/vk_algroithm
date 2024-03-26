array = [1, 2, 3, 4, 5, 6]

def reverse_array_full(arr):
    left, right = 0, len(arr) - 1
    while left < right:
        arr[left], arr[right] = arr[right], arr[left]
        left += 1
        right -= 1
    return arr

reversed_array = reverse_array_full(array)
print(reversed_array) 
