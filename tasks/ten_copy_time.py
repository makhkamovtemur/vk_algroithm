def min_time_to_copy(n, x, y):
    if x > y:
        x, y = y, x

    def can_copy_in_time(t):
        return (t // x) + (t // y) >= n - 1  # n-1, потому что одна копия уже есть

    # Начальные и конечные границы времени
    left, right = 0, n * y
    while left < right:
        mid = (left + right) // 2
        if can_copy_in_time(mid):
            right = mid
        else:
            left = mid + 1
    return left + min(x,y)